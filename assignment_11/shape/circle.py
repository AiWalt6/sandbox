import math

from shape import Shape


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def __str__(self):
        return f'{super().__str__()} (Circle)'
