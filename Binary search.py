# Есть ли введенное число в списке

from random import randint

def binary_search(s, item):
    found = False
    first = 0
    last = len(s) - 1
    while first <= last and not found:
        midpoint = (first + last) // 2
        if s[midpoint] == item:
            return f'Число {n} в списке присутствует'
        else:
            if item < s[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    if not found:
        return f'Число {n} в списке отсутствует'


a = [randint(1, 100) for i in range(10)]
print(a)
a.sort()
n = int(input("Введите число: "))
print(binary_search(a, n))
