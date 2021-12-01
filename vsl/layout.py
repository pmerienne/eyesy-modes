import pygame

from vsl import atom, sys
from vsl.utils import to_absolute

from vsl.color import *


def grid(
        nb_columns=2,
        nb_rows=2,
        cell=lambda row, col: atom.rectangle((0.1, 0.1), 0.9, 0.9, WHITE)
    ):
    full_width, full_height = sys.screen.get_size()
    cell_width = int(full_width / nb_columns)
    cell_height = int(full_height / nb_rows)

    for row in range(nb_rows):
        for col in range(nb_columns):
            x = int(col * cell_width)
            y = int(row * cell_height)
            position = (x, y)
            rect = (position, (cell_width, cell_height))
            with screen_context(rect):
                cell(row, col)


def symmetry(
        horizontal=True,
        vertical=True,
        bg_color=None,  # TODO
        content_function=lambda: atom.circle(0.5, 0.9, 0.7, RED)):
    full_width, full_height = sys.screen.get_size()

    # Draw first screen
    if horizontal and vertical:
        content_size = full_width / 2, full_height / 2
    elif horizontal:
        content_size = full_width, full_height / 2
    else:  # Vertical
        content_size = full_width / 2, full_height
    content_width, content_height = content_size[0], content_size[1]

    content_rect = ((0.0, 0.0), content_size)
    with screen_context(content_rect):
        content_function()
        content_surface = sys.screen

    # Draw symmetric
    if horizontal and vertical:
        sys.screen.blit(pygame.transform.flip(content_surface, 1, 0), (content_width, 0))  # Top Right
        sys.screen.blit(pygame.transform.flip(content_surface, 0, 1), (0, content_height))  # Bottom Left
        sys.screen.blit(pygame.transform.flip(content_surface, 1, 1), (content_width, content_height))  # Bottom Right
    elif horizontal:
        sys.screen.blit(pygame.transform.flip(content_surface, 0, 1), (0, content_height))  # Bottom
    else:  # Vertical
        sys.screen.blit(pygame.transform.flip(content_surface, 1, 0), (content_width, 0))  # Right




def scene(
        relative_x=0.0,
        relative_y=0.0,
        relative_width=0.5,
        relative_height=0.5,
        bg_color=None,
        content_function=lambda: atom.rectangle(0.0, 0.0, 1.0, 1.0, WHITE)):
    position = to_absolute((relative_x, relative_y))
    size = to_absolute((relative_width, relative_height))
    rect = (position, size)

    with screen_context(rect):
        if bg_color is not None:
            bg_color = typing.color(bg_color)
            sys.screen.fill(bg_color)
        content_function()


class screen_context(object):
    def __init__(self, rect):
        self.rect = rect
        self.previous_screen = None

    def __enter__(self):
        self.previous_screen = sys.screen
        sys.screen = self.previous_screen.subsurface(self.rect)

    def __exit__(self, *args):
        sys.screen = self.previous_screen
