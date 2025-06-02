from packages.Shapes import (Point, Line, Rectangle, Square, Triangle, Equilateral, Isosceles, Scalene)

def print_section(title, shape):
    print("=" * 40)
    print(f"{title:^40}")
    print("=" * 40)
    print(shape)
    print("\n")

def main():
    try:
        # Rectangle
        rectangle = Rectangle(
            [Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)],
            [
                Line(Point(0, 0), Point(1, 0)),
                Line(Point(1, 0), Point(1, 1)),
                Line(Point(1, 1), Point(0, 1)),
                Line(Point(0, 1), Point(0, 0)),
            ],
        )
        print_section("Rectángulo", rectangle)

        # Square
        square = Square(
            [Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)],
            [
                Line(Point(0, 0), Point(1, 0)),
                Line(Point(1, 0), Point(1, 1)),
                Line(Point(1, 1), Point(0, 1)),
                Line(Point(0, 1), Point(0, 0)),
            ],
        )
        print_section("Cuadrado", square)

        # Triangle
        triangle = Triangle(
            False,
            [Point(0, 0), Point(1, 0), Point(0, 1)],
            [
                Line(Point(0, 0), Point(1, 0)),
                Line(Point(1, 0), Point(0, 1)),
                Line(Point(0, 1), Point(0, 0)),
            ],
        )
        print_section("Triángulo", triangle)

        # Equilateral
        equilateral = Equilateral(
            [Point(0, 0), Point(1, 0), Point(0.5, (3 ** 0.5) / 2)],
            Line(Point(0, 0), Point(1, 0)),
        )
        print_section("Equilátero", equilateral)

        # Isosceles
        isosceles = Isosceles(
            [Point(0, 0), Point(1, 0), Point(0.5, (3 ** 0.5) / 2)],
            Line(Point(0, 0), Point(1, 0)),
        )
        print_section("Isósceles", isosceles)

        # Scalene
        scalene = Scalene(
            [Point(0, 0), Point(1, 0), Point(0.5, (3 ** 0.5) / 2)],
            [
                Line(Point(0, 0), Point(1, 0)),
                Line(Point(1, 0), Point(0.5, (3 ** 0.5) / 2)),
                Line(Point(0.5, (3 ** 0.5) / 2), Point(0, 0)),
            ],
        )
        print_section("Escaleno", scalene)
    except Exception as e:
        print(f"An error occurred: {e}, try again")
        
        
if __name__ == "__main__":
    main()