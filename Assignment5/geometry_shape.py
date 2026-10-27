import math
import turtle

SQUARE = "1"
CIRCLE = "2"
TRIANGLE = "3"
QUIT = "4"


def main():
    display_menu()
    while (choice := input("Enter your choice: ").strip()) != QUIT:
        if choice == SQUARE or choice == TRIANGLE:
            x = get_number("Enter the starting X coordinate: ")
            y = get_number("Enter the starting Y coordinate: ")
            side = get_number("Enter the length of a side: ", True)
            color = get_color()
            if choice == SQUARE:
                square(x, y, side, color)
            else:
                equilateral_triangle(x, y, side, color)
        elif choice == CIRCLE:
            x = get_number("Enter the X coordinate of the center: ")
            y = get_number("Enter the Y coordinate of the center: ")
            radius = get_number("Enter the radius: ", True)
            color = get_color()
            circle(x, y, radius, color)
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
        display_menu()

    print("Exiting the program.")
    turtle.done()


def display_menu():
    print()
    print("Shape Menu")
    print("1) Draw a Square")
    print("2) Draw a Circle")
    print("3) Draw an Equilateral Triangle")
    print("4) Quit")


def square(x, y, side, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()


def equilateral_triangle(x, y, side, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(3):
        turtle.forward(side)
        turtle.left(120)
    turtle.end_fill()


def circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.setheading(0)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def get_number(prompt, positive=False):
    while True:
        try:
            number = float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a number.")
        else:
            if not math.isfinite(number):
                print("Invalid number. Please enter a finite number.")
            elif positive and number <= 0:
                print("Invalid size. Please enter a number greater than zero.")
            else:
                return number


def get_color():
    while True:
        color = input("Enter the fill color: ").strip()
        if color == "":
            print("Invalid color. Please enter a turtle color such as red, blue, or green.")
        else:
            try:
                turtle.fillcolor(color)
            except turtle.TurtleGraphicsError:
                print("Invalid color. Please enter a turtle color such as red, blue, or green.")
            else:
                return color


if __name__ == "__main__":
    main()
