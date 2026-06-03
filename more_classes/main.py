   from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159265359 * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, side_1, height):
        self.side_1 = side_1
        self.height = height

    def area(self):
        return (self.side_1 * self.height) / 2


class Trapeze(Shape):
    def __init__(self, side_1, side_2, height):
        self.side_1 = side_1
        self.side_2 = side_2
        self.height = height

    def area(self):
        return (self.side_1 + self.side_2) * self.height / 2


class Square(Shape):
    def __init__(self, side_1):
        self.side_1 = side_1

    def area(self):
        return self.side_1 ** 2


if __name__ == '__main__':
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(5, 6),
        Trapeze(4, 6, 5),
        Square(5)
    ]

    for shape in shapes:
        print("Area:", shape.area())