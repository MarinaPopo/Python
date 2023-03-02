import math

class Sphere:
    def __init__(self, r, x, y, z):
        self.r = r
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return 4 / 3 * math.pi * self.r ** 3

    def get_square(self):
        return 4 * math.pi * self.r ** 2

    def get_radius(self):
        return self.r

    def set_raduis(self, r):
        self.r = r

    def get_center(self):
        return self.x, self.y, self.z

    def set_center(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def is_point_inside(self, x, y, z):
        if (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2 <= self.r ** 2:
            return True
        else:
            return False


sphere1 = Sphere(0.6, 0, 0, 0)
print(f"get_raduis: {sphere1.get_radius()}")
print(f"get_volume: {sphere1.get_volume()}")
print(f"get_square: {sphere1.get_square()}")
print(f"get_center: {sphere1.get_center()}")
print(f"is_point_inside (0, -1.5, 0): {sphere1.is_point_inside(0, -1.5, 0)}")
sphere1.set_raduis(1.6)
print(f"set_radius(1.6): {sphere1.get_radius()}")
print(f"is_point_inside (0, -1.5, 0): {sphere1.is_point_inside(0, -1.5, 0)}")
