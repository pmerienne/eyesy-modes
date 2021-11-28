import math


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
