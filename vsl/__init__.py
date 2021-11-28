_screen = None
_etc = None


def clear_scene(screen, etc):
    global _screen, _etc
    _screen = screen
    _etc = etc


def get_etc():
    return _etc


def get_screen():
    return _screen
