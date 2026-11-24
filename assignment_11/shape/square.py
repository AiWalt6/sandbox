from shape import Shape


class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.__side = side

    def get_area(self):
        return self.__side ** 2

    def __str__(self):
        return f'{super().__str__()} (Square)'
