# Класс прямоугольника с методами для площади, периметра, диагонали, рисования
from math import sqrt



class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        print(f"Периметр прямоугольника: {(self.a + self.b) * 2}")

    def area(self):
        print(f"Площадь прямоугольника: {self.a * self.b}")

    def diagonal(self):
        print(f"Диагональ прямоугольника: {round(sqrt(self.a ** 2 + self.b ** 2), 2)}")

    def draw_rectangle(self):
        i = 0
        while i < self.a:
            print("*" * self.b)
            i += 1


a = int(input("Длина прямоугольника: "))
b = int(input("Ширина прямоугольника: "))
rect1 = Rectangle (a, b)
rect1.area()
rect1.perimeter()
rect1.diagonal()
rect1.draw_rectangle()
