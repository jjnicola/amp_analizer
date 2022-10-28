import numpy as np
from scipy.io import wavfile
from  matplotlib import pyplot as plt
import scipy
import scipy.fftpack

class Analyzer():
    def __init__(self):
        self.audio_data = None
        self.fs = None
        self.fft_out = None

    def load_file(self):
        self.fs, self.audio_data = read("output.wav")
        numpy.array(self.audio_data[1],dtype=float)
        print ("Frequency sampling", fs)

    def plot(self):

        fs_rate, signal = wavfile.read("output.wav")
        print ("Frequency sampling", fs_rate)
        l_audio = len(signal.shape)
        print ("Channels", l_audio)
        if l_audio == 2:
            signal = signal.sum(axis=1) / 2
        N = signal.shape[0]
        print ("Complete Samplings N", N)
        secs = N / float(fs_rate)
        print ("secs", secs)
        Ts = 1.0/fs_rate # sampling interval in time
        print ("Timestep between samples Ts", Ts)
        t = np.arange(0, secs, Ts) # time vector as scipy arange field / numpy.ndarray
        FFT = abs(np.fft.fft(signal))
        FFT_side = FFT[range(int(N/2))] # one side FFT range
        freqs = scipy.fftpack.fftfreq(signal.size, t[1]-t[0])
        fft_freqs = np.array(freqs)
        freqs_side = freqs[range(int(N/2))] # one side frequency range
        fft_freqs_side = np.array(freqs_side)
        plt.subplot(311)
        p1 = plt.plot(t, signal, "g") # plotting the signal
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.subplot(312)
        p2 = plt.plot(freqs, FFT, "r") # plotting the complete fft spectrum
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Count dbl-sided')
        plt.subplot(313)
        p3 = plt.plot(freqs_side, abs(FFT_side), "b") # plotting the positive fft spectrum
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Count single-sided')
        plt.show()


    def plot_2(self):

        fs_rate, signal = wavfile.read("file.wav")
        print ("Frequency sampling", fs_rate)
        l_audio = len(signal.shape)
        print ("Channels", l_audio)
        if l_audio == 2:
            signal = signal.sum(axis=1) / 2
        N = signal.shape[0]
        print ("Complete Samplings N", N)
        secs = N / float(fs_rate)
        print ("secs", secs)
        Ts = 1.0/fs_rate # sampling interval in time
        print ("Timestep between samples Ts", Ts)
        t = np.arange(0, secs, Ts) # time vector as scipy arange field / numpy.ndarray

        total_samples = int(fs_rate * secs)
        dt = t[1] - t[0]

        apply_blackman_window = True
        signal_blackman = signal
        frq = np.fft.fftfreq(total_samples, dt)

        if (apply_blackman_window == True):
            signal_blackman = signal * np.blackman(total_samples)
            signal_blackman = np.append(signal_blackman, np.zeros(4* total_samples))
            t = np.linspace (0, secs * 5 /2 + 4*dt , 5* total_samples)
            frq = np.fft.fftfreq(5 * total_samples, dt)
        
        FFT = np.fft.fft(signal_blackman) / int(5 * total_samples)

        fig = plt.figure(figsize=(6, 8))

        t_zero_pad = np.linspace (0, secs * 5 /2 + 4*dt , 5* total_samples)

        ax1 = fig.add_subplot(211)
        ax1.plot(t, signal_blackman)
        plt.xlabel('Frecuencia (Hz)')
        plt.ylabel('$signal(t)$')

        ax2 = fig.add_subplot(212)
        ax2.vlines(frq, 0, abs(FFT))  # Espectro de amplitud
        plt.xlabel('Frecuencia (Hz)')
        plt.ylabel('Abs($FFT$)')
        plt.show()

if __name__ == "__main__":
    a = Analyzer()
    a.plot_2()
