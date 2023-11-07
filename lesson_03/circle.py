import math

from lesson_03.shape import Shape


class Circle(Shape):
    _radius: float

    def __init__(self, radius, name: str):
        super().__init__(name)
        self._radius = radius

    def get_perimeter(self) -> float:
        return 2 * math.pi * self._radius

    def get_area(self) -> float:
        return math.pi * self._radius ** 2
