from vsl import sys


def color(_color):
    if isinstance(_color, float) or isinstance(_color, int):
        _color = sys.etc.color_picker(_color)

    _color = (
        int(_color[0]),
        int(_color[1]),
        int(_color[2])
    )
    return _color
