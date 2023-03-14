class Second:
    def __init__(self, sec):
        self.sec = sec

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        d = (self.sec // 86400)
        if d < 1:
            return f"{Second.__get_form(h)}:{Second.__get_form(m)}:{Second.__get_form(s)}"

        else:
            return f"{d} дн. {Second.__get_form(h)}:{Second.__get_form(m)}:{Second.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __sub__(self, other):
        return Second(self.sec - other.sec)

    def __mul__(self, other):
        return Second(self.sec * other.sec)

    def __floordiv__(self, other):
        return Second(self.sec // other.sec)

    def __mod__(self, other):
        return Second(self.sec % other.sec)

    def __ISUB__(self, other):
        return Second(self.sec - other.sec)

    def __IMUL__(self, other):
        return Second(self.sec * other.sec)

    def __IFLOORDIV__(self, other):
        return Second(self.sec // other.sec)

    def __IMOD__(self, other):
        return Second(self.sec % other.sec)


c1 = Second(600)
c2 = Second(200)
print(f"c1: {c1.get_format_time()}")
print(f"c2: {c2.get_format_time()}")
c3 = c1 - c2
print(f"c1 - c2: {c3.get_format_time()}")
c3 = c1 * c2
print(f"c1 * c2: {c3.get_format_time()}")
c3 = c1 // c2
print(f"c1 // c2: {c3.get_format_time()}")
c3 = c1 % c2
print(f"c1 % c2: {c3.get_format_time()}")
c1 -= c2
print(f"c1 -= c2: {c1.get_format_time()}")
c1 *= c2
print(f"c1 *= c2: {c1.get_format_time()}")
c1 //= c2
print(f"c1 //= c2: {c1.get_format_time()}")
c1 %= c2
print(f"c1 %= c2: {c1.get_format_time()}")
