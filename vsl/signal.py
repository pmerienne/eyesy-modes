import math
import time


def elapsed_ms():
    return round(time.time() * 1000)


def sawtooth(min=0.0, max=1.0, step=0.001):
    assert max >= min
    interval = max - min
    total = elapsed_ms() * step
    current = math.fmod(total, interval)
    return current


def lfo(min=0.0, max=1.0, step=0.001, phase=0.0):
    assert max >= min
    interval = 2.0 * (max - min)  # Forward + Backward
    total = phase + (elapsed_ms() * step)
    current = min + math.fmod(total, interval)

    if current > max:  # We're going backward
        current = max - (current - max)
    if current < min or current > max:
        print('NOT POSSIBLE')
    return current
