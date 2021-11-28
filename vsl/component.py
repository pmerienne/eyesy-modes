import math

import pygame

from vsl import typing, system
from vsl.utils import rotate


def rotated_rect(
        position=(0, 0),
        width=50,
        height=100,
        color=0,
        angle=0,
        fill=True,
        thickness=0,
    ):
    # Clean input
    color = typing.color(color)

    # Get rect points
    a = position[0], position[1]
    b = position[0] + width, position[1]
    c = position[0] + width, position[1] + height
    d = position[0], position[1] + height

    # Rotate points
    points = [
        a,
        rotate(b, center=a, angle=angle),
        rotate(c, center=a, angle=angle),
        rotate(d, center=a, angle=angle),
    ]
    pygame.draw.polygon(system.screen, color, points, 0 if fill else thickness)


def sun(
        position=(0.0, 0.0),
        radius=0.25,
        color=0,
        nb_rays=20,
        ray_radius=0.25,
        ray_colors=[0.20, 0.45],
    ):
    color = typing.color(color)

    # Draw rays
    angle_step = 2.0 * math.pi / nb_rays
    for i in range(nb_rays):
        ray_color = ray_colors[i % len(ray_colors)]
        sun_ray(
            center=position,
            length=ray_radius,
            start_angle=i * angle_step,
            end_angle=(i + 1) * angle_step,
            color=ray_color,
        )

    # Draw center
    position = system.to_absolute(position)
    radius = system.to_absolute(radius)
    pygame.draw.circle(system.screen, color, position, radius)


def sun_ray(
        center=(0.0, 0.0),
        length=0.25,
        start_angle=0.0,
        end_angle=2*math.pi/6.0,
        fill=True,
        thickness=0,
        color=0
    ):
    """
    Actually draw an isosceles triangle
    :param color:
    :param thickness:
    :param fill:
    :param center:
    :param length:
    :param start_angle:
    :param end_angle:
    :return:
    """
    color = typing.color(color)

    a = center
    b = rotate((center[0], center[1] + length), center, start_angle)
    c = rotate((center[0], center[1] + length), center, end_angle)

    points = [a, b, c]
    points = system.to_absolute_points(points)
    pygame.draw.polygon(system.screen, color, points, 0 if fill else thickness)
