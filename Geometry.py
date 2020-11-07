import math
def locate_1d(distance1, distance2, base_length):
    angle = math.acos((distance1 ^ 2 + base_length ^ 2 - distance2 ^ 2) / (2 * distance1 * base_length))
    x = distance1 * math.cos(angle)
    return x

def as_distance(amplitude, conversion):
    '''
    Convert amplitude to distance.
    An amplitude of 0 is considered to be infinitely far away from the microphone.
    Distance grows inversely with amplitude, scaled by a conversion factor
    '''
    if amplitude == 0:
        return math.inf
    return (1 / amplitude) * conversion

