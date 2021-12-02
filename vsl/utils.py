import math

import pygame

from vsl import sys


def rotate(point, center, angle):
    """
    Rotate a point around a center
    :param point: point to rotate (as a x, y tuple)
    :param center: center of rotation (as a x, y tuple)
    :param angle: angle of rotation ([0, 2PI])
    :return: new point (as a x, y tuple)
    """
    px, py, cx, cy = point[0], point[1], center[0], center[1]
    new_x = math.cos(angle) * (px-cx) - math.sin(angle) * (py-cy) + cx
    new_y = math.sin(angle) * (px-cx) + math.cos(angle) * (py-cy) + cy
    return new_x, new_y


def blit_rotate(target, surface, target_position, surface_pivot, angle):
    """
    Rotate and blit a surface into another.
    Copy/Paste from https://stackoverflow.com/questions/59909942/how-can-you-rotate-an-image-around-an-off-center-pivot-in-pygame/59909946#59909946
    :param target: target Surface
    :param surface: Surface which has to be rotated and blit
    :param target_position: position of the pivot on the target Surface surf (relative to the top left of main_surface)
    :param surface_pivot: is position of the pivot on the Surface to rotate (relative to the top left of surface)
    :param angle: angle in degree
    :return:
    """
    image_rect = surface.get_rect(topleft=(target_position[0] - surface_pivot[0], target_position[1] - surface_pivot[1]))
    offset_center_to_pivot = pygame.math.Vector2(target_position) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (target_position[0] - rotated_offset.x, target_position[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(surface, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
    target.blit(rotated_image, rotated_image_rect)




def to_absolute_points(points):
    return [to_absolute(point) for point in points]


def to_absolute(relative_value):
    width, height = sys.screen.get_size()

    if isinstance(relative_value, float):
        return int(relative_value * width)
    elif isinstance(relative_value, (list, tuple)) and len(relative_value) == 2:
        return (
            int(relative_value[0] * width),
            int(relative_value[1] * height),
        )
    else:
        return [
            int(v * width)
            for v in relative_value
        ]


def clip(value, min_value, max_value):
    if value < min_value:
        return min_value
    elif value > max_value:
        return max_value
    else:
        return value


