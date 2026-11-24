from shape import Shape


class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.__base = base
        self.__height = height

    def get_area(self):
        return self.__base * self.__height / 2

    def __str__(self):
        return f'{super().__str__()} (Triangle)'
