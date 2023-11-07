from lesson_03.shape import Shape


class Triangle(Shape):
    __slots__ = ("_side_a", "_side_b", "_side_c")

    def __init__(self, side_a, side_b, side_c, name: str):
        biggest_size = max(side_a, side_b, side_c)
        if biggest_size > (side_a + side_b + side_c - biggest_size):
            raise ValueError()
        super().__init__(name)
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    def get_perimeter(self) -> float:
        return self._side_a + self._side_b + self._side_c

    def get_area(self) -> float:
        semi_perimeter = self.get_perimeter() / 2
        return ((semi_perimeter - self._side_a) * (semi_perimeter - self._side_b) * (
                    semi_perimeter - self._side_c) * semi_perimeter) ** 0.5
