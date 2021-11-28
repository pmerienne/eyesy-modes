from vsl.layout import *
from vsl.signal import *


def setup(screen, etc):
    system.setup(screen, etc)


def draw(screen, etc):
    # Draw background
    etc.bg_color = BLACK

    # One sun
    grid(
        nb_columns=7,
        nb_rows=7,
        cell=lambda row, col: atom.circle(
            lfo(min=0.4, max=0.6, step=0.0001) if row % 2 == 1 else 0.5,
            0.5,
            0.2,
            color_mix(PURPLE, BLUEVIOLET, lfo(step=0.0005, phase=0.1 * row + 0.1 * col))
        )
    )
    time.sleep(0.02)

