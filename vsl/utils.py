import math

from vsl import system


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


def to_absolute_points(points):
    return [to_absolute(point) for point in points]


def to_absolute(relative_value):
    width, height = system.screen.get_size()

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


