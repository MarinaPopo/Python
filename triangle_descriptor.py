class NonNegative:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError('Нужно указать положительное целое число')
        instance.__dict__[self.name] = value


class Triangle:
    a = NonNegative()
    b = NonNegative()
    c = NonNegative()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def if_exist(self):
        if self.a + self.b < self.c or self.a + self.c < self.b or self.c + self.b < self.a:
            print(f"Треугольник со сторонами {self.a, self.b, self.c} не существует")
        else:
            print(f"Треугольник со сторонами {self.a, self.b, self.c} существует")


triangle1 = Triangle(2, 5, 6)
triangle2 = Triangle(5, 2, 8)
triangle3 = Triangle(7, 3, 6)
triangle1.if_exist()
triangle2.if_exist()
triangle3.if_exist()
