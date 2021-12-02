from vsl import *


def setup(screen, etc):
    sys.setup(screen, etc)


def draw(screen, etc):
    # Draw background
    etc.bg_color = BLACK

    symmetry(
        lambda: sun(
            x=lfo(min=-0.15, max=1.15, step=0.00005),
            y=0.10,
            radius=0.05,
            color=(0, 0, 0),
            ray_radius=2.0,
            ray_colors=[WHITE, RED],
        ),
        horizontal=True,
        vertical=False,
    )
