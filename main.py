import Geometry
import Microphone
import SignalProcessing
import GUI

def sample_for(freq, distance_constant):
    def on_sample(left, right):
        left_fft = SignalProcessing.do_FFT(left, Microphone.RATE)
        right_fft = SignalProcessing.do_FFT(right, Microphone.RATE)

        left_amplitude = left_fft[freq]
        right_amplitude = right_fft[freq]

        left_distance = Geometry.as_distance(left_amplitude, distance_constant)
        right_distance = Geometry.as_distance(right_amplitude, distance_constant)

        x = Geometry.locate_1d(left_distance, right_distance)
        print(x)


if __name__ == "__main__":
    Microphone.printMicrophones()
    Microphone.record_LR_continuous(sample_for(400, 1), lambda : False, 1, 2)

