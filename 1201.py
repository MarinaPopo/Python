# Функция принимает аргумент, затем умножается

def func_compute(n):
    return lambda x: x * n


res = func_compute(2)
print(res(15))
print(res(20))
res = func_compute(3)
print(res(15))
print(res(20))


# Лямбда-выражение для произведения трех чисел

# mult = (lambda x: lambda y: lambda z: x * y * z)
# print(mult(2)(5)(5))


# Сортируем список студентов

# students = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98}
# ]
#
# print(sorted(students, key=lambda item: item['name']))
# print(sorted(students, key=lambda item: item['final'], reverse=True))

# Мин и макс оценка

# students = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98}
# ]
# print(sorted(students, key=lambda item: item['final'])[-1])
# print(sorted(students, key=lambda item: item['final'])[0])
