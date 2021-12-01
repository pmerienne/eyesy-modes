from vsl import *


def setup(screen, etc):
    sys.setup(screen, etc)


def draw(screen, etc):
    # Draw background
    etc.bg_color = BLACK

    symmetry(
        horizontal=True,
        vertical=False,
        content_function=lambda: sun(
            x=lfo(min=-0.15, max=1.15, step=0.00005),
            y=0.10,
            radius=0.05,
            color=(0, 0, 0),
            ray_radius=2.0,
            ray_colors=[WHITE, RED],
        )
    )

    time.sleep(0.02)

