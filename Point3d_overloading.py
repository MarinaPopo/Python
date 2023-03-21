class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point3D(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Point3D(x, y, z)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return Point3D(x, y, z)

    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        z = self.z / other.z
        return Point3D(x, y, z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z


point1 = Point3D(12, 15, 18)
point2 = Point3D(6, 3, 9)
print(f"Координаты 1-й точки: {point1.x}, {point1.y}, {point1.z}")
print(f"Координаты 2-й точки: {point2.x}, {point2.y}, {point2.z}")
point3 = point1 + point2
print(f"Сложение координат: {point3.x, point3.y, point3.z}")
point3 = point1 - point2
print(f"Вычитание координат: {point3.x, point3.y, point3.z}")
point3 = point1 * point2
print(f"Умножение координат: {point3.x, point3.y, point3.z}")
point3 = point1 / point2
print(f"Деление координат: {point3.x, point3.y, point3.z}")
print(f"Равенство координат: {point1 == point2}")
print(f"x = {point1.x} x1 = {point2.x}")
print(f"y = {point1.y} y1 = {point2.y}")
print(f"z = {point1.z} z1 = {point2.z}")
point1.x = 20
print(f"Запись значения в координату x: {point1.x}")