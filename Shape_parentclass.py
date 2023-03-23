from abc import abstractmethod
from math import sqrt


class Shape:
    def __init__(self, a, b, color):
        self.a = a
        self.b = b
        self.color = color

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def draw(self):
        for k in range(self.a):
            for j in range(self.b):
                print('*', end="")
            print()

    def info(self):
        print(f"Цвет: {self.color}\nПериметр: {self.perimeter()}\nПлощадь: {self.area()}")
        self.draw()


class Square(Shape):
    def __init__(self, a, color):
        self.a = self.b = a
        self.color = color

    def info(self):
        print("===Квадрат===")
        print(f"Сторона: {self.a}")
        super().info()
        print()


class Rectangle(Shape):
    def info(self):
        print("==Прямоугольник")
        print(f"Длина: {self.a}\nШирина: {self.b}")
        super().info()
        print()


class Triagle(Shape):
    def __init__(self, a, b, c, color):
        self.c = c
        super().__init__(a, b, color)

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return round(sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 2)

    def draw(self):
        rows = []
        for n in range(self.b):
            rows.append(" " * n + "*" * (self.a - 2 * n))
        print("\n".join(reversed(rows)))


    def info(self):
        print("===Треугольник===")
        print(f"Сторона 1: {self.a}\nСторона 2: {self.b}\nСторона 3: {self.c}")
        super().info()
        print()


shapes = [
    Square(3, 'red'),
    Rectangle(3, 7, 'green'),
    Triagle(11, 6, 6, 'yellow')
]

for shape in shapes:
    shape.info()
