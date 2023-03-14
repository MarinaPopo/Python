import math


class Pair:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    def summa(self):
        return self.a + self.b

    def mult(self):
        return self.a * self.b


class RightTriangle(Pair):

    def __init__(self, a, b):
        super().__init__(a, b)

    def hypotenuse(self):
        return print(f"Гипотенуза треугольника: {math.sqrt(self.a ** 2 + self.b ** 2):.2f}")

    def area(self):
        return print(f"Площадь треугольника: {super().mult() / 2:.2f}")

    def info(self):
        print(f"Прямоугольный треугольник ({self.a}, {self.b}, {math.sqrt(self.a ** 2 + self.b ** 2):.2f}")


triangle = RightTriangle(5, 8)
triangle.hypotenuse()
triangle.info()
triangle.area()
print(f"Сумма: {triangle.summa()}")
print(f"Произведение: {triangle.mult()}")
print()
triangle.a = 10
triangle.b = 20
triangle.hypotenuse()
triangle.info()
triangle.area()
print(f"Сумма: {triangle.summa()}")
print(f"Произведение: {triangle.mult()}")

