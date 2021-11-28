from vsl import get_etc


def color(_color):
    etc = get_etc()

    if isinstance(_color, float) or isinstance(_color, int):
        _color = etc.color_picker(_color)

    _color = (
        int(_color[0]),
        int(_color[1]),
        int(_color[2])
    )
    return _color


def position(_position):
    return (
        int(_position[0]),
        int(_position[1])
    )
