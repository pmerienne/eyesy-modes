import pygame

from vsl import sys, typing

from vsl.utils import to_absolute, to_absolute_points


def rectangle(relative_x, relative_y, relative_width, relative_height, color):
    color = typing.color(color)
    position = to_absolute((relative_x, relative_y))
    size = (to_absolute(relative_width), to_absolute(relative_height))
    rect = (position, size)
    return pygame.draw.rect(sys.screen, color, rect)


def circle(
        relative_x,
        relative_y,
        relative_radius,
        color
    ):
    position = to_absolute((relative_x, relative_y))
    radius = to_absolute(relative_radius)
    color = typing.color(color)
    pygame.draw.circle(sys.screen, color, position, radius)


def polygon(
        relative_points,
        color,
        fill=True,
        thickness=0,
    ):
    points = to_absolute_points(relative_points)
    color = typing.color(color)
    pygame.draw.polygon(sys.screen, color, points, 0 if fill else thickness)

