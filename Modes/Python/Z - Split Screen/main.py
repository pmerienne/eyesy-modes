from vsl.layout import *
from vsl.signal import *


def setup(screen, etc):
    system.setup(screen, etc)


def draw(screen, etc):
    # Draw background
    etc.color_picker_bg(etc.knob5)

    # One sun
    grid(
        nb_columns=7,
        nb_rows=7,
        cell=lambda row, col: atom.circle(
            lfo(min=0.2, max=0.8, step=0.0001),
            0.5,
            0.2,
            (lfo(min=35, max=70, step=0.01, phase=row), lfo(min=30, max=125, step=0.01, phase=3*col), 178)
        )
    )
    time.sleep(0.02)

