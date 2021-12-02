from vsl import *


def setup(screen, etc):
    sys.setup(screen, etc)


def draw(screen, etc):
    # Draw background
    etc.bg_color = WHITE

    kaleidoscope(
        lambda: sun(
            x=lfo(min=0.1, max=0.3, step=0.00005),
            y=0.10,
            color=(0, 0, 0),
            radius=0.10,
            ray_radius=0.80,
            ray_colors=[WHITE, RED],
        )
    )

    time.sleep(0.02)

