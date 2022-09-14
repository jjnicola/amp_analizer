import pyaudio  
import wave
import sys

macros = []
if sys.version_info[:2] >= (3, 10):  # https://bugs.python.org/issue40943
    macros.append(("PY_SSIZE_T_CLEAN", None))

def play_audio_sample():
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
         
         
         
def run_profiler():
    play_audio_sample()

if __name__ == "__main__":
    run_profiler()
