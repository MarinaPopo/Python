class Student:
    def __init__(self, name):
        self.name = name
        self.laptop = self.Laptop()

    def show(self):
        print(self.name, end=" ")
        self.laptop.show()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i7"
            self.ram = 16

        def show(self):
            print(f" => {self.brand}, {self.cpu}, {self.ram}")


s1 = Student("Roman")
s2 = Student("Vladimir")

s1.show()
s2.show()