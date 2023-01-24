# Импорт для всех задач:
from random import randint

# Веденное число есть в списке?

# a = [int(input("-> ")) for i in range(int(input("Введите элементы списка: \nn = ")))]
# num = int(input("Введите число: "))
# if num in a:
#     print("Есть такое число")
# else:
#     print("Нет такого значения")

# Сумма элементов списка
#
# a = [randint(1,100) for i in range(20)]
# res = 0
# for i in a:
#     res += i
# print(a)
# print(res)

# По убыванию

# a = [randint(0, 100) for i in range(10)]
# print(a)
# a.sort(reverse=True)
# print(a)


# Произведение ненулевых в матрице

# matrix = [[randint(0, 4) for row in range(3)] for col in range(4)]
# mult = 1
# for row in matrix:
#     for col in row:
#         print(col, end="\t\t")
#         if col != 0:
#             mult *= col
#     print()
# print("Произведение ненулевых элементов:", mult)


# Диагональ

# n = int(input("Размерность массива: "))
# matrix = [[randint(1, 100) for row in range(n)] for col in range(n)]
# print("Массив из случайных чисел от 1 до 100:")
# for row in matrix:
#     for col in row:
#         print(col, end="\t")
#     print()
# diagonal = []
# for i in range(n):
#     diagonal.append(matrix[i][i])
# print(diagonal)
# print("Минимальный элемент диагонали:", min(diagonal))


# Считаем отрицательные

# matrix = [[randint(-20, 10) for row in range(3)] for col in range(4)]
# neg = 0
# for row in matrix:
#     for col in row:
#         print(col, end="\t\t")
#         if col < 0:
#             neg += 1
#     print()
# print("Количество отрицательных эл-тов:", neg)
