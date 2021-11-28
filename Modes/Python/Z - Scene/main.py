from vsl import system
from vsl.component import *
from vsl.signal import *


def setup(screen, etc):
    system.setup(screen, etc)


def draw(screen, etc):
    # Draw background
    etc.color_picker_bg(etc.knob5)

    # One sun
    sun(
        position=(500, lfo(min=0, max=etc.yres)),
        color=etc.color_picker(etc.knob4),
        radius=int(etc.knob1 * 80)
    )
    time.sleep(0.02)

