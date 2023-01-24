def area1(a, b, c):
    def area_rect(x, y):
        return x * y

    s1 = 2 * (area_rect(a, b) + area_rect(b, c) + area_rect(a, c))
    return s1


def area2(a, b, c):
    s2 = 1

    def area_rect(x, y, z):
        nonlocal s2
        s2 = 2 * (x * y + y * z + x * z)

    area_rect(a, b, c)
    return s2


s3 = 1


def area3(a, b, c):
    def area_rect(x, y):
        return x * y

    global s3
    s3 = 2 * (area_rect(a, b) + area_rect(b, c) + area_rect(a, c))
    return s3


print(area1(2, 4, 6))
print(area2(5, 8, 2))
print(area3(1, 6, 8))




