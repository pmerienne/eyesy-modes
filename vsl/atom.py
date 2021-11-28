import pygame

from vsl import system, typing

from vsl.utils import to_absolute, to_absolute_points


def rectangle(relative_position, relative_width, relative_height, color):
    color = typing.color(color)
    position = to_absolute(relative_position)
    size = (to_absolute(relative_width), to_absolute(relative_height))
    rect = (position, size)
    return pygame.draw.rect(system.screen, color, rect)


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

