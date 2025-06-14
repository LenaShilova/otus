from math import sqrt
from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Triangle sides can't be less than 0")
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("Triangle doesn't exist")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        s = self.perimeter / 2
        return sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
