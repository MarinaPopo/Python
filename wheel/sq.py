class Square:
    def __init__(self, a):
        self.a = a

    def get_perimetr(self):
        return 4 * self.a


s1 = Square(50)
print(s1.get_perimetr())