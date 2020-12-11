import Microphone
import SignalProcessing
import Geometry
import matplotlib.pyplot as plt
import numpy as np

sound_speed_in_sec = 343
base_distance = 0.175

plt.ion()
f = Microphone.RATE * np.arange((Microphone.CHUNK / 2)) / Microphone.CHUNK

angle = []
toa = []
def handler(dataL, dataR):

    #Scale signals so that they are the same amplitude
    dataL = (dataL - np.mean(dataL))/np.std(dataL)
    dataR = (dataR - np.mean(dataR))/np.std(dataR)

    correlation = SignalProcessing.correlate(dataL, dataR)
    time_diff = SignalProcessing.time_difference(correlation, Microphone.RATE)
    toa.append(time_diff)
    angle.append(Geometry.locate_1d_toa(time_diff, sound_speed_in_sec, base_distance))

    if len(angle) > 100:
        angle.pop(0)
    if len(toa) > 100:
        toa.pop(0)
    plt.figure("Angle")
    plt.clf()
    plt.plot(angle)
    plt.draw()

    plt.figure("Microphones")
    plt.clf()
    plt.plot(dataR)
    plt.plot(dataL)

    plt.figure("Time difference")
    plt.clf()
    plt.plot(toa)
    plt.draw()

    plt.figure("Correlation")
    plt.clf()
    plt.plot(correlation)
    plt.draw()

    plt.pause(0.005)

plt.show()

Microphone.record_LR_continuous(handler, lambda : False, 1, 2)

