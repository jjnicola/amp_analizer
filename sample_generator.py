from math import log10
import numpy as np
from scipy import signal
import struct
from scipy.io import wavfile

def create_profiler_1 ():
    rate = 44100
    sec_per_freq = 1
    samples = rate * sec_per_freq
    x = np.arange(samples)
    
    with open('profiler.wav', 'wb') as f:
        
        for power in range (2,5):
            base_range = range(1,10)
            for i in base_range:
                freq = int(10**power * log10(i) if i != 1 else 10**(power-1))
                y = 100* np.sin(2 * np.pi * freq * x / rate)
                for i in y:
                    f.write(struct.pack('b', int(i)))

def create_profiler_2 ():

    samplerate = 44100; fs = 100
    t = np.linspace(0., .1, samplerate)
    amplitude = np.iinfo(np.int16).max
    data = amplitude * np.sin(2. * np.pi * fs * t)
    wavfile.write("profiler.wav", samplerate, data.astype(np.int16))



def create_profiler_3 ():
    rate = 44100
    t = np.linspace(0., 1., int(rate))

    complete = []
    for power in range (2,5):
        base_range = range(1,10)
        
        for i in base_range:
            freq = int(10**power * log10(i) if i != 1 else 10**(power-1))
            amplitude = np.iinfo(np.int16).max
            chunk = amplitude * np.sin(2. * np.pi * freq * t)
            complete=np.append(complete,chunk)


    wavfile.write("profiler.wav", rate, complete.astype(np.int16))

if __name__ == "__main__":
    create_profiler_3 ()
