import pygame

from vsl import system, typing

from vsl.utils import to_absolute, to_absolute_points


def circle(
        relative_position,
        relative_radius,
        color
    ):
    position = to_absolute(relative_position)
    radius = to_absolute(relative_radius)
    color = typing.color(color)
    pygame.draw.circle(system.screen, color, position, radius)


def polygon(
        relative_points,
        color,
        fill=True,
        thickness=0,
    ):
    points = to_absolute_points(relative_points)
    color = typing.color(color)
    pygame.draw.polygon(system.screen, color, points, 0 if fill else thickness)