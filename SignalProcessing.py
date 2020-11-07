import numpy as np
import numpy.fft as fft


def do_FFT(signal, samplingRate):
    Y_k = np.fft.fft(signal)[0:int(len(signal) / 2)] / len(signal)  # FFT function from numpy
    Y_k[1:] = 2 * Y_k[1:]  # need to take the single-sided spectrum only
    Pxx = np.abs(Y_k)  # be sure to get rid of imaginary part

    f = samplingRate * np.arange((len(signal) / 2)) / len(signal)  # frequency vector
    return (f, Pxx)



