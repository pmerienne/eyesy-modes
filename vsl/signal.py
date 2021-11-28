import math
import time


def elapsed_ms():
    return round(time.time() * 1000)


def sawtooth(min=0.0, max=1.0, step=0.1):
    assert max >= min
    interval = max - min
    total = elapsed_ms() * step
    current = math.fmod(total, interval)
    return current


def lfo(min=0.0, max=1.0, step=0.1):
    assert max >= min
    interval = 2 * (max - min)  # Forward + Backward
    total = elapsed_ms() * step
    current = math.fmod(total, interval)

    if current > max:  # We're going backward
        current = max - (current - max)
    return current
