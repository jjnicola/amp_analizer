import pyaudio
import wave
import sys
from threading import Thread
import os, signal

class PlayRec():
    def __init__(self):
        self.RECORDING = True

    def signal_handler (self, sig, frame):
        print ("pid %d got sigint", os.getpid())
        self.RECORDING = False


    def record_audio(self):
            CHUNK = 1024
            FORMAT = pyaudio.paInt16
            CHANNELS = 1
            RATE = 44100
            RECORD_SECONDS = 30
            WAVE_OUTPUT_FILENAME = "output.wav"

            p = pyaudio.PyAudio()

            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)

            print("* recording")

            frames = []
            while self.RECORDING:
                data = stream.read(CHUNK)
                frames.append(data)

            print("* done recording")

            stream.stop_stream()
            stream.close()
            p.terminate()

            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

            sys.exit(0)

    def play_audio_sample(self):
        #define stream chunk
        chunk = 1024
        #open a wav format music
        f = wave.open(r"./profiler.wav","rb")

        #instantiate PyAudio
        p = pyaudio.PyAudio()

        #open stream
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                        channels = f.getnchannels(),
                        rate = f.getframerate(),
                        output = True)
        #read data
        data = f.readframes(chunk)

        #play stream
        while data:
            stream.write(data)
            data = f.readframes(chunk)

        #stop stream
        stream.stop_stream()
        stream.close()

        #close PyAudio
        p.terminate()
        sys.exit(0)
