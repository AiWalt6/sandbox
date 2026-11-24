from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle


def main():
    shapes = [
        Rectangle('rect1', 4, 5),
        Circle('circle1', 3),
        Rectangle('rect2', 4, 4),
        Circle('circle2', 1.5),
        Square('square1', 4),
        Triangle('triangle1', 4, 5),
    ]

    print('Areas of various shapes:')
    for shape in shapes:
        print(f'{shape.__class__.__name__} area: {shape.get_area():.2f}')


if __name__ == '__main__':
    main()
