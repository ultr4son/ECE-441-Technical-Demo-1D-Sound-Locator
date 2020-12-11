import math


def locate_1d_ratio(amplitude1, amplitude2, base):
    '''
    Get the position of the sound as a ratio between the two microphone amplitudes scaled by a unit
    '''
    if amplitude1 == 0 or amplitude2 == 0:
        return None

    #Amplitudes that are the same would be at the center of the two microphones (0)
    if amplitude1 > amplitude2:
        return (amplitude1/amplitude2 - 1) * base
    else:
        return (-amplitude2/amplitude1 + 1) * base

def locate_1d_toa(time_difference, sound_speed, base_distance):
    costheta = (time_difference * sound_speed)/base_distance
    if(math.fabs(costheta) > 1):
        return 0
    return math.degrees(math.acos((time_difference * sound_speed)/base_distance))

def as_distance(amplitude, conversion):
    '''
    Convert amplitude to distance.
    An amplitude of 0 is considered to be infinitely far away from the microphone.
    Distance grows inversely with amplitude, scaled by a conversion factor
    '''
    if amplitude == 0:
        return math.inf
    return (1 / amplitude) * conversion

