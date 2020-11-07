
import pyaudio
import numpy as np
import speech_recognition
import matplotlib.pyplot as plot

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

def getMicrophones():
    return [pyaudio.PyAudio().get_device_info_by_index(i) for i in range(pyaudio.PyAudio().get_device_count())]

def printMicrophones():
    microphones = getMicrophones()
    for mic in microphones:
        print(str(mic.get('index') + ": " + str(mic.get('name'))))

def record_one(device_index):
    stream = p.open(format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
        input_device_index = device_index
    )
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    # data = data * np.hanning(len(data))
    stream.stop_stream()
    stream.close()
    return data


def record(seconds, device_index):
    stream = p.open(format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
        input_device_index = device_index
    )
    frames = []

    for i in range(0, int(RATE / CHUNK * seconds)):
        data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
        frames.extend(data)
    stream.stop_stream()
    stream.close()

    return frames

def record_continuous(sample_handler, stop_recording, device_index):
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=device_index,
                    )
    while not stop_recording():
        data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
        sample_handler(data)
    stream.stop_stream()
    stream.close()

def record_LR_continuous(sample_handler, stop_recording, deviceL_index, deviceR_index):
    left_stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index= deviceL_index,
                    )
    right_stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=deviceR_index,
                    )
    while not stop_recording():
        dataL = np.fromstring(left_stream.read(CHUNK), dtype=np.int16)
        dataR = np.fromstring(right_stream.read(CHUNK), dtype=np.int16)
        sample_handler(dataL, dataR)

    left_stream.stop_stream()
    left_stream.close()

    right_stream.stop_stream()
    right_stream.close()

