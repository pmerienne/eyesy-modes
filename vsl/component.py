from vsl.utils import rotate
from vsl import atom
from vsl.color import *


def h_lines(
        nb_lines=5,
        colors=[ORANGE, BLUE, GREEN]
    ):
    y_step = 1.0 / float(nb_lines)
    for i in range(nb_lines):
        color = colors[i % len(colors)]
        atom.rectangle(0.0, i * y_step, 1.0, y_step, color)


def sun(
        x=0.0,
        y=0.0,
        radius=0.25,
        color=0,
        nb_rays=20,
        ray_radius=0.25,
        ray_colors=(GOLD, MAROON),
    ):

    # Draw rays
    angle_step = 2.0 * math.pi / nb_rays
    for i in range(nb_rays):
        ray_color = ray_colors[i % len(ray_colors)]
        sun_ray(
            x=x,
            y=y,
            length=ray_radius,
            start_angle=i * angle_step,
            end_angle=(i + 1) * angle_step,
            color=ray_color,
        )

    # Draw center
    atom.circle(x, y, radius, color)


def sun_ray(
        x=0.0,
        y=0.0,
        length=0.25,
        start_angle=0.0,
        end_angle=2*math.pi/6.0,
        color=0
    ):
    """
    Actually draw an isosceles triangle
    :param color:
    :param center:
    :param length:
    :param start_angle:
    :param end_angle:
    :return:
    """
    center = (x, y)
    a = center
    b = rotate((x, y + length), center, start_angle)
    c = rotate((x, y + length), center, end_angle)

    points = [a, b, c]
    atom.polygon(points, color)
