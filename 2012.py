from math import pi


def rectangle(x, y):
    return x * y


def triangle(x, y):
    return x * y / 2


def circle(x):
    return x * x * pi


s = input("1 - прямоугольник, 2 - треугольник, 3 - круг: ")

if s == "1":
    a = float(input("Первая сторона: "))
    b = float(input("Вторая сторона: "))
    print("Площадь:", rectangle(a, b))

elif s == "2":
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    print("Площадь:", triangle(a, h))

elif s == "3":
    r = float(input("Радиус: "))
    print("Площадь:", circle(r))
