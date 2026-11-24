from shape import Shape


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def __str__(self):
        return f'{super().__str__()} (Rectangle)'
