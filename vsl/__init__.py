class System:
    def __init__(self):
        self.screen = None
        self.etc = None

    def setup(self, screen, etc):
        self.screen = screen
        self.etc = etc

    def sub_screen(self, position, width, height):
        rect = (position, (width, height))
        return SubScreen(rect)


system = System()


class SubScreen:
    def __init__(self, rect):
        self.rect = rect
        self.previous_screen = None

    def __enter__(self):
        self.previous_screen = system.screen
        system.screen = self.previous_screen.subsurface(self.rect)

    def __exit__(self, *args):
        system.screen = self.previous_screen
