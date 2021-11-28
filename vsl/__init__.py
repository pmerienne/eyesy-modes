class System:
    def __init__(self):
        self.screen = None
        self.etc = None

    def setup(self, screen, etc):
        self.screen = screen
        self.etc = etc

    def to_absolute_points(self, points):
        return [self.to_absolute(point) for point in points]

    def to_absolute(self, value):
        width, height = self.screen.get_size()

        if isinstance(value, float):
            return self._to_absolute(value, width)
        elif isinstance(value, (list, tuple)) and len(value) == 2:
            return (
                self._to_absolute(value[0], width),
                self._to_absolute(value[1], height),
            )
        else:
            return [
                self._to_absolute(v, width)
                for v in value
            ]

    def _to_absolute(self, relative_value, max_value=None):
        """
        Convert a relative value [0.0, 1.0] to an absolute value [0, max_value]
        :param value: float
        :return: int
        """
        max_value = max_value or self.screen.get_width()
        return int(relative_value * max_value)


system = System()

