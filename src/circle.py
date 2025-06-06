from figure import Figure


class Circle(Figure):

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Circle radius can't be less than 0")
        self.radius = radius
        self.pi = 3.14

    @property
    def area(self):
        return self.pi * (self.radius ** 2)

    @property
    def perimeter(self):
        return 2 * self.pi * self.radius


circle = Circle(2)
