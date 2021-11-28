from vsl.component import *
from vsl.signal import *


def setup(screen, etc):
    system.setup(screen, etc)


def draw(screen, etc):
    # Draw background
    etc.color_picker_bg(1.0)

    # One sun
    sun(
        position=(lfo(min=0.1, max=0.3, step=0.00005), 0.10),
        color=(0, 0, 0),
        radius=0.10,
        ray_radius=0.80,
        ray_colors=[0.15, 0.45],
    )
    time.sleep(0.02)

