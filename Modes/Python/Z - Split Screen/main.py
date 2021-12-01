from vsl import *


def setup(screen, etc):
    sys.setup(screen, etc)


def draw(screen, etc):
    # Draw background
    etc.bg_color = BLACK

    scene(
        relative_x=lfo(min=0.0, max=0.4, step=0.00005),
        relative_y=0.1,
        relative_width=0.3,
        relative_height=0.1,
        bg_color=RED,
        content_function=lambda: sun(
            x=lfo(min=-0.15, max=1.15, step=0.00005),
            y=0.10,
            radius=0.05,
            color=(0, 0, 0),
            ray_radius=2.0,
            ray_colors=[WHITE, RED],
        )
    )

    scene(
        relative_x=0.72,
        relative_y=0.1,
        relative_width=0.26,
        relative_height=0.8,
        bg_color=BLACK,
        content_function=lambda: sun(
            x=1.4,
            y=lfo(min=-1.0, max=2.0, step=0.0001),
            color=(0, 0, 0),
            ray_radius=2.0,
            ray_colors=[BLACK, RED],
        )
    )

    scene(
        relative_x=0.0,
        relative_y=0.22,
        relative_width=0.70,
        relative_height=0.76,
        bg_color=BLACK,
        content_function=lambda: sun(
            x=lfo(min=-1.0, max=2.0, step=0.0001),
            y=1.4,
            color=(0, 0, 0),
            ray_radius=2.0,
            ray_colors=[BLACK, WHITE],
        )
    )

    time.sleep(0.02)

