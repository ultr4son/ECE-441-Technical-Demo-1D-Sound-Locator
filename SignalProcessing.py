import numpy as np
import numpy.fft as fft
from bisect import bisect_left


def do_FFT(signal, samplingRate):
    '''
    Perform an FFT on the time domain signal
    '''
    Y_k = np.fft.fft(signal)[0:int(len(signal) / 2)] / len(signal)  # FFT function from numpy
    Y_k[1:] = 2 * Y_k[1:]  # need to take the single-sided spectrum only
    Pxx = np.abs(Y_k)  # be sure to get rid of imaginary part

    f = samplingRate * np.arange((len(signal) / 2)) / len(signal)  # frequency vector
    return (f, Pxx)

def correlate(signal1, signal2):
    return np.correlate(signal1, signal2, 'full')

def time_difference(correlation, sampling_frequency):
    '''
    Detemine the time of arrival difference between two signals.
    '''
    return (np.argmax(correlation) - len(correlation) / 2)/ sampling_frequency

def max_amplitude(magnitudes, frequencies, fL, fH):
    '''
    Select the max amplitude of an fft in a range of frequencies
    '''
    li = bisect_left(frequencies, fL)
    hi = bisect_left(frequencies, fH)
    if len(magnitudes[li:hi]) > 0:
        return max(magnitudes[li:hi])
    return 0