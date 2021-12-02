import pygame

from vsl import atom, sys
from vsl.utils import blit_rotate
from vsl.color import *
from vsl.layout import screen_context, surface_context


def symmetry(
        horizontal=True,
        vertical=True,
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


def kaleidoscope(content_function):
    """
    Kaleidoscope effect made by constructing an hexagon containing 12 triangles of the same content.
    :param content_function:
    :return:
    """
    full_size = sys.screen.get_size()
    quadrant_size = full_size[0] / 2, full_size[1] / 2
    quadrant_diagonal = math.ceil(math.sqrt(quadrant_size[0] ** 2 + quadrant_size[1] ** 2))
    content_size = quadrant_diagonal, quadrant_diagonal
    content_width = content_size[0]
    content_height = content_size[1]

    # Draw main content on a surface
    with surface_context(content_size):
        content_function()
        content_surface = sys.screen

    # Surface is a rectangle, we need a triangle content.
    # Thus, we use a triangle mask with alpha to "select" content
    # See https://stackoverflow.com/questions/40682775/how-does-one-stretch-an-image-to-the-shape-of-a-polygon-in-pygame
    op = math.tan(math.pi / 6.0) * content_width
    triangle = [
        (0, 0),
        (0, content_height),
        (op, 0)
    ]
    mask = pygame.Surface(content_size, pygame.SRCALPHA)
    pygame.draw.polygon(mask, WHITE, triangle)
    content_surface.blit(mask, (0, 0), None, pygame.BLEND_RGBA_MULT)

    # We'll now blit this triangle 12 times
    # Rotating every triangle more and more
    # 1 triangle on 2 will be flipped horizontally
    target_pivot_position = full_size[0] / 2, full_size[1] / 2
    angle_step = 360.0 / 12.0
    for i in range(12):
        triangle_content = content_surface.copy()

        if i % 2 == 0:
            surface_pivot_position = 0, content_height
            angle = math.floor(-float(i) * angle_step)
        else:
            # Flip horizontally one on two
            surface_pivot_position = content_width, content_height
            angle = math.floor(-float(i + 1) * angle_step)
            triangle_content = pygame.transform.flip(triangle_content, 1, 0)

        blit_rotate(sys.screen, triangle_content, target_pivot_position, surface_pivot_position, angle)
