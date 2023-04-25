# name = "Marina"  # создание переменной
# age = 20
# print("Hello,", name)
# print(type(age))
import json
import math
import re
import time

# a = b = c = 1
# print(a, b, c)
#
# a, b, c = "Hello", 5, False
# print(a, b, c)
#
# PI = 3.14
# print(PI)
# PI = 2

# name = "Марина"
# age = 21
# print("Меня зовут " + name + ", мне " + str(age))

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# # a, b = b, a
# c = a
# a = b
# b = c
# print("a:", a)
# print("b:", b)

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3)
# print(s3 * 3)

# print(5356456456456456644)
# print(53.56456456456456644)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2) # 3.0
# print(6 // 2) # 3
# print(6 // 5) # 1
# print(6 / 5) # 1.2
# print(6 ** 2)
# print(7 % 2)

# a, b, c = 5, 7, 3
# summa = a + b + c
# pro = a * b * c
# sredn = summa // 3
# print ("Сумма:", summa)
# print ("Произведение:", pro)
# print ("Среднее арифметическое:", sredn)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)

# num = 10
# num += 5  # num = num + 5
# print(num)  # 15
#
# num -= 3
# print(num)  # 12

# num = 4321
# a = num % 10
# num = num // 10
# b = num % 10
# num = num // 10
# c = num % 10
# num = num // 10
# d = num % 10
#
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)

# a, b = 1, 2
# a = a + b
# b = a - b
# a = a - b
# print("a:", a)
# print("b:", b)

# Функции явного преобразования типов
# int()
# str()
# float()
# bool()

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# print(res)
#
# print(int(3.8))
# a = 3.8
# print(type(round(a)))
# print(round(3.831, 2))

# a = 1
# b = 2
# print("a:", a, "\nb:", b)

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep = "", end= " ")
# print("Я учу Python.")
#
# name = input("Введите имя: ")
# print("Hello", name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно", res)

# print("Введите четыре числа:")
# a = int(input("1: "))
# b = int(input("2: "))
# c = int(input("3: "))
# d = int(input("4: "))
# print("Ответ:", round((a+ b)/(c + d), 2))

# b1 = True #1
# b2 = False #2
# print(b1 + 5) # 1 + 5 = 6
# print(b2 + 5) # 0 + 5 = 5

# print(bool("python"))
# print(bool("")) # False
# print(bool(" "))
# print(bool(5))
# print(bool(0)) # False
# print(bool(False)) # False
# print(bool(None)) # False
#
# test = None
# print(test)
# test = 5

# print(7 == 7)
# print(2 + 5 == 7)
# print("привет" > "Привет")

# print(2 < 4 < 9)
# print(2 * 5 > 7 >= 4 + 3)
# print(3 * 3 <= 7 >= 2)

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)
# print(not 9 - 5) # False
# print(not 7 - 7) #

# cnt = 15
# if cnt < 10:
#     cnt += 1
#     print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 35
# b = 35
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("a = b")

# a = int(input("Введите первую сторону: "))
# b = int(input("Введите вторую сторону: "))
# c = int(input("Введите третью сторону: "))
# if a == b == c:
#     print("Это равносторонний треугольник")
# elif a == b or a == c or c == b:
#     print("Это равнобедренный треугольник")
# else:
#     print("Это разносторонний треугольник")
#
# day = int(input("Введите день недели цифрой: "))
# if 1 <= day <= 5:
#     print("Это рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Это выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Это некорректное значение")

# month = int(input("Введите номер месяца: "))
# if month == 1 or month == 2 or month == 12:
#     print("Зима")
# elif 3 <= month <= 5:
#     print("Весна")
# elif 6 <= month <= 8:
#     print("Лето")
# elif 9 <= month <= 11:
#     print("Осень")
# else:
#     print("Нет такого месяца")
# month = int(input("Введите номер месяца: "))
# if 1 <= month <= 12:
#     if month == 1 or month == 2 or month == 12:
#         print("Зима")
#     if 3 <= month <= 5:
#         print("Весна")
#     if 6 <= month <= 8:
#         print("Лето")
#     if 9 <= month <= 11:
#         print("Осень")
# else:
#     print("Нет такого месяца")

# n = int(input("Сколько ворон сидит на ветке? "))
# if 0 <= n <= 9:
#     print("На ветке", n, end=" ")
#     if n == 1:
#         print("ворона")
#     if 2 <= n <= 4:
#         print("вороны")
#     if 5 <= n <= 9 or n == 0:
#         print("ворон")
# else:
#     print("Ошибка ввода данных")

# a, b = 30, 20
# minim = a if a < b else b
# print(minim)

# a, b = 30, 30
# minim = "a == b" if a == b else "a > b" if a > b else "b > a"
# print(minim)

# a = int(input("Введите делимое: "))
# b = int(input("Введите делитель: "))
# res = a / b if b != 0 else "На ноль делить нельзя"
# print(res)

# Исключения

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Что-то пошло не так")
# except ZeroDivisionError:
#     print("На ноль делить нельзя")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или делить на ноль")
# else:
#     print("Все нормально. Вы ввели", n, "и", m)  # если в try не возникли исключения, только с except
# finally:
#     print("Конец программы")  # в любом случае, м.б. без except

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
#
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)


# Цикл while

# while условие:
#   тело цикла

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1 # i = i + 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# i = 2
# while i <= 20:
#     print("i =", i)
#     i += 2

# n = int(input("Введите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1
#
# n = int(input("Введите количество символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1


# start = int(input('Start: '))
# end = int(input('End: '))
# i = start
# sum_ = 0
# while i <= end:
#     if i%2:
#         sum_ += i
#     i += 1
# print('Summa:', sum_)

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Четное число")
# else:
#     print("Нечетное число")

# i = 0
# while i < 10:
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while i < 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i, end=" ")
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# mult = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     mult *= n
#
# print("Произведение:", mult)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# kol = int(input("Введите количество чисел последовательности: "))
# ch = float(input("Введите число: "))
# i = 1
# min_ = ch
# max_ = ch
# sum_ = ch
# while i < kol:
#     ch = float(input("Введите число: "))
#     sum_ += ch
#     if ch < min_:
#         min_ = ch
#     if ch > max_:
#         max_ = ch
#     i += 1
#
# print("Количество чисел: ", kol)
# print("Минимальное число: ", min_)
# print("Максимальное число: ", max_)
# print("Среднее арифметическое: ", sum_/kol)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, "\t\t", end="")
#         j += 1
#     print()
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         if j == 9:
#             print(f'{i} * {j} = {i * j}')
#         else:
#             print(f'{i} * {j} = {i * j}', end='\t')
#         j += 1
#     i += 1
#
# for element in collection:
#   тело цикла

# for i in 'Hello':
#     print(i)

# for color in 'red', 'orange', 'yellow', 'green', 1, 20, 0.3:
#     print("color: ", color)

# range(start, end, step)

# print(range(1, 3))

# for i in range(1, 10, 2):
#     print(i, end=" ")
#
# print()
#
# i = 1
# while i < 10:
#     print(i, end=" ")
#     i += 2

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")
#
# for i in range(11, 100, 11):
#     print(i, end=" ")
#
# for i in range(1, 100):
#     if i % 11 == 0:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("done")

# Вложенный for
#
# for i in range(3):
#     print("+++", i)
#     for j in range(2):
#         print("-----", j)

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
#
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# letter = [i for i in "Hello"]
# print(letter)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Списки (list)
# nums = [8, 3, 9, 4, 1, "Hello", 4.3]
# print(nums)
# print(nums[0])
# print(nums[-1])
# nums[1] = 256
# print(nums)
# nums[3] += 100 # Добавили к значению индекса это значение
# print(nums)
# print(len(nums))

# s = []
# print(s)
#
# s1 = list()
# print(s1)
#
# s2 = list("Hello")

# s = [1, 3, 5]
# print(s)
# n = s * 6
# print(n)

# n = list(range(10))
# print(n)

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# c = [i * 3 for i in "list"]
# print(c)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input("Число: ")
# print(a)

# a = [input("-> ") for i in range(int(input("Введите количество элементов списка: ")))]
# print(a)

# a = [8, 4, 2, 9, 1]
# for i in range(len(a)):
#     print(a[i], end=" ")
# print()
# for elem in a:
#     print(elem, end=" ")

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# summa = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         summa += a[i]
# print("Сумма отрицательных чисел:", summa)

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# summa = 0
# for i in a:
#     if i < 0:
#         summa += i
# print("Сумма отрицательных чисел:", summa)

# a = list(range(21, 41))
# print(a)
# even = 0
# odd = 0
# for i in a:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += i
# print("Количество четных: ", even)
# print("Сумма нечетных: ", odd)

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# n = 0
# summa = 0
# for i in a:
#     summa += i
#     if i != 0:
#         n += 1
# print("Среднее арифметическое:", summa/n)

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [7, 8, 2, 1, 17]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)

# список[start:end:step]

# a = [7, 8, 2, 1, 17, 9]
# print(a[1:4])
# print(a[0::1])
# print(a[::2])
# print(a[::-1])

# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:])
# print(s[-3:1:-1])
# print(s[2:5])

# a = [7, 8, 2, 1, 17, 9]
# a[1:3] = [0, 0, 0, 0]
# print(a)
# a[1:2] = [20]
# print(a)
# a[2] = 50
# print(a)
# del a[2]
# print(a)
# del a[2:4]
# print(a)
# del a[:]
# print(a)

# Методы списков
# print(dir(list))

# s = [7, 8, 2, 1, 17, 9]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # добавляет список элементов в конец списка
# print(s)
# s.extend("add")
# print(s)
# s.insert(0, 100)  # добавляем элемент по индексу - (индекс, значение)
# print(s)

# a = [1, 2, 3]
# n = int(input("n = "))
# for i in range(n):
#     # x = input("-> ")
#     # a.append(x)
#     a.append(int(input("-->"))
# print(a)

# [a.append(int(input("-> "))) for i in range(int(input("n = ")))]
# print(a)

# a = []
# for i in range(int(input("Кол-во эл-тов списка: "))):
#     n = int(input("Введите число, кратное 3: "))
#     if n % 3:
#         a.append(n)
#     else:
#         print(n, "не делится на 3 без остатка")
# print(a)
#
# n = int(input('Кол-во элементов списка: '))
# lst = []
#
# for i in range(n):
#     d = int(input('Введите число кратное 3: '))
#     lst.append(d) if not d % 3 else print(f'Число {d} не делится на 3 без остатка')
#
# print(lst)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 4, 2]
# c = []
# if len(b) > len(a)
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(b[i])
# print(c)

# a = [1, 2, 3, 4, 2, 55, 99]
# a.remove(2)  # Удаляет первый встретившийся элемент по значению
# print(a)
# last = a.pop()  # Удаляет и возвращает элемент (по умолчанию - последний)
# print(a)
# print(last)
# a.clear()  # удаляет из списка все элементы

# a = [int(input("-> ")) for i in range(int(input("Введите элементы списка: ")))]
# k = int(input("Введите индекс: "))
# a.pop(k)
# print(a)

# a = [5, 9, 7, 6]
# s = 0
# for i in a:
#     s += i
# print(s)

# a = []
# [a.append(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# while True:
#     if len(a) == 0:
#         break
#     k = int(input("Введите индекс: \nk = "))
#     a.pop(k)
#     print(a)

# a = [5, 9, 7, 6, 9, 4, 9, 0, 9]
# # print(a)
# # num = a.count(9)  # кол-во заданных значений в списке
# # print(num)
# # ind = a.index(9, 4)  # возвращает индекс первого вхождения значения с индекса
# # # (или без индекса), если не найдено: ValueError
# # print(ind)
# # ch = 3
# # if ch in a:
# #     ind = a.index(ch)
# #     print(ind)

# a = [5, 9, 7]
# b = a
# b.append(120)
# print("a = ", a)
# print("b = ", b)
# print(id(a))
# print(id(b))

# a = [5, 9, 7]
# b = a.copy() # создает копию списка
# b.append(120)
# print("a = ", a)
# print("b = ", b)
# print(id(a))
# print(id(b))

# a = [5, 9, 7, 6, 9, 4, 9, 0, 9]
# a.reverse()  # в обратном порядке
# print(a)
# a.sort()  # сортирует список по умолчанию по возрастанию
# print(a)
# a.sort(reverse=True)
# print(a)
# b = sorted(a)
# print(b)
# print(a)

#
#
# s = ['Виталий', 'Сергей', 'Александр', 'Анна']
# print(s)
# s.sort(key=len, reverse=True)
# print(s)

# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(0, 9))  # включительно, нельзя указать одно число
# print(random.randrange(9))  # от 0 до 9, исключая 9
# print(random.randrange(2, 9))  # от 2 до 9, исключая 9
# print(random.randrange(0, 10, 2))  # от 0 до 10 с шагом 2

# from random import randint, randrange
#
# print(randint(1, 9))
# print(randrange(9))

# from random import *
# print(randint(1, 9))
# print(randrange(9))

# import random as r
# print(r.randint(1, 9))
# print(r.randrange(9))
# print(r.uniform(10.5, 25.5))
#
# city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(r.choice(city))
# print(r.choices(city, k=3))
# r.shuffle(city)
# print(city)

# import random as r
#
# mas = [r.randint(50000, 100000) for i in range(10)]
# print(mas)

# lst = [9, 12, 1, 11, 14]
# print(min(lst))
# print(max(lst))
# print(sum(lst))

# import random as r

# a = [r.randint(1, 100) for i in range(10)]
# print(a)
# b = max(a)
# print("Max:", b)
# a.remove(b)
# a.insert(0, b)
# print(a)

# a = [r.randint(-20, 20) for i in range(10)]
# print(a)
# a.sort(reverse=True)
# print(a)
#
# a = [r.randint(1, 100) for i in range(10)]
# print(a)
# b = min(a)
# k = a.index(b)
# print("Min:", b)
# print("Index:", k)
# a = a[k:]  # или del a[:k]
# print(a)

# x = list('1dfdf34fg5')
# print(x)
# print('a' in x)
# print('a' not in x)
#
# lst = []
# if len(lst) == 0:
#     print("Список пустой")
#
# if not lst:
#     print("Список пустой")

# import random as r
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [r.randint(0, 10) for i in range(n1)]
# b = [r.randint(0, 10) for i in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# c = b + a
# print("Общий список:", c)
#
# c = []
#
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Список без повторений:", c)
#
# c = []
#
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print("Элементы общие для двух списков", c)
#
# c = []
#
# c = [min(a), max(a), min(b), max(b)]
# print("Макс. и мин. обоих списков:", c)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# # print(m[1][2])
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x ** 2, end="\t")
#     print()

# w, h = 10, 10
# matrix = [[x*y for x in range(1, w)] for y in range(1, h)]
# # matrix = []
# # for y in range(h):
# #     new_row = []
# #     for x in range(w):
# #         new_row.append(0)
# #     matrix.append(new_row)
#
#
# for h in matrix:
#     for w in h:
#         print(w, end="\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# import random
# n = int(input("Размерность матрицы: "))
# mas = []
# for i in range(n):
#     mas.append([])
#     for j in range(n):
#         mas[i].append(random.randint(1, 100))
#
# for row in mas:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
# m = 101
# lst = []
# for k in range(n):
#     if m > mas[k][k]:  # Диагональ
#         lst.append(mas[k][k])
# print(lst, end="\t")
# print("\n", min(lst))

# import math
#
# num1 = math.ceil(3.2)  # округление в большую сторону
# num2 = math.floor(3.8)  # округление в меньшую сторону
# num3 = math.sqrt(2)  # квадратный корень
# print(num1)
# print(num2)
# print(num3)
#
# from math import pi
#
# r = int(input("Введите радиус окружности: "))
# print("Длина окружности:", round(2 * pi * r, 2))

# import time

# second = time.time()
# a = 10293848489
# print(second)
# local_time = time.ctime(2671522092)
# print(local_time)
# res = time.localtime()
# print(res)
# print(res.tm_mon, res.tm_year)
# print(time.strftime("Today is %B %d, %Y", time.localtime(a)))
# print(time.strftime("%d/%m/%Y, %H:%M:%S"))

# pause = 5
# print("Запуск программы")
# time.sleep(pause)
# print(pause, "сек.")

# text = input("Название напоминаия: ")
# local_time = float(input("Через сколько минут: "))
# time.sleep(local_time * 60)
# print(text)

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)

# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")
#
# print(time.strftime("Сегодня %B %d, %Y"))


# Функции


# def hello(name, age):
#     print("Hello, ", name, ". I am ", age, sep="")
#
#
# hello("Irina", 20)
# hello("Ivan", 23)

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum('abc', 'hello')

# def symbol(n, a, b):
# for i in range(n):
#     if i % 2:
#         print(b, end="")
#     else:
#         print(a, end="")
# print()
# Второй вариант
# def symbol(n, a, b):
# [print(b, end='') if i % 2 else print(a, end='') for i in range(n)]
# print()

# Третий вариант
# def symbol(n, a, b):
#     for i in range(n):
#         print(a, end="")
#         a, b = b, a
#     print()
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")


# def get_sum(a, b):
#     if a > b:
#         return True
#     else:
#         return False
#
#
# x = 150
# y = 70
# if get_sum(x, y):
#     print(x, "больше", y)
# else:
#     print(y, "больше", x)

# def get_sum(a, b):
#     if a > b:
#         return True
#     else:
#         return False
#
#
# x = int(input("a = "))
# y = int(input("b = "))
#
# if get_sum(x, y):
#     print(x - y)
# else:
#     print(x + y)

# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def change(lst):
#     # lst[-1], lst[0] = lst[0], lst[-1]
#     n = lst.pop()
#     m = lst.pop(0)
#     lst.insert(0, n)
#     lst.append(m)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_number = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_number = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_number:
#         return True
#     else:
#         return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")

# def get_sum(a, b, c, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5, 2, d=2))

# def set_param(c=20, s="-"):
#     for i in range(c):
#         print(s, end="")
#     print()
#
# set_param(s="+")
# set_param(5, "*")

# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         num = n % 10
#         if even and num % 2 == 0:
#             s += num
#         if not even and num % 2 != 0:
#             s += num
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр: ")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
#
#
# print("Сумма нечетных цифр: ")
# print(digit_sum(9874023, False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))
#
# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(age=23, name="Ira")
# display_info(age=23, name="Ira")

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
#
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# a = "Hello"
# b = "Hello"
# print(a == b)
# print(a is b)

# s = "Hello"
# print(s, id(s))
# s += "World"
# print(s, id(s))

# s = "Hello"
# print(s[1])
# s[1] = "a"  # Не получится

# print(id(s))
# s = s[1:-1]
# print(s, id(s))

# def add_number(n):
#     print("Внутри функции: ", n, id(n))
#     n += 1
#     print("Измененное значение: ", n, id(n))
#     return n
#
#
# x = 1
# print("До функции:", x, id(x))
# add_number(x)
# print("После функции:", x, id(x))

# def add_number(n):
#     print("Внутри функции: ", n, id(n))
#     n = n + [4]
#     print("Измененное значение: ", n, id(n))
#
#
# x = [1, 2, 3]
# print("До функции:", x, id(x))
# add_number(x)
# print("После функции:", x, id(x))

# Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst)
# print(tpl)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (1, 2, 3, 4, 5)
# print(a[0])
# print(a[1:3])
#
#
# s = tuple(int(input("-> ")) for i in range(3))
# print(s)

# from random import  randint
#
# s = tuple(randint(1, 20) for i in range(10))
# print(s)

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t3.count("l"))
# print(t3.index("l"))
#
# if "w" in t3:
#     print(t3.index("w"))
# else:
#     print("Такого символа нет")

# for i in t3:
#     print(i * 2, end=" ")
# print("\n", t3)

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# from random import randint
#
# def create_tuple(l, start, end):
#     return tuple(randint(start, end) for i in range(l))
#
#
# t1 = create_tuple(10, 0, 5)
# t2 = create_tuple(5, -5, 0)
# t3 = t1 + t2
# print(t1)
# print(t2)
# print(t3)
# print(t3.count(0))

# t = (10, "Hello", [1, 2, 3], (4, 5, 6), ["hello", "world"])
# print(t, id(t))
# t[-1][0] = "new"
# print(t, id(t))
# t[4].append("hi")
# print(t, id(t))
#
# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married


# user = get_user()
# print(user)
# name1, age1, is_married1 = user
# print(name1, age1, is_married1)

# name2, age2, is_married2 = get_user()
# print(name2, age2, is_married2)

# t = (1, 2, 3)
# t = list(t)
# t.append(4)
# t = tuple(t)
# print(t)


# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
#
# for country in countries:
#     countryName, countryPopulation, cities = country
#     print("\nСтрана", countryName, "с населением", countryPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print("\tГород", cityName, "с населением", cityPopulation)


# Множество (set) - неупорядоченный, только уникальные

# s = {"banana", "apple", "orange"}
# print(type(s))
# print(s)

# s = {x * x for x in range(10)}
# print(s)

# numbers = [1, 2, 2, 2, 3, 3, 4,4, 5, 6]
# # num = {i for i in numbers if i % 2 == 0}
# num = list(set(numbers))
# print(num)

# def to_set(a):
#     return set(a), len(set(a))
#
#
# print(to_set("я обычная строка"))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t = {'red', 'green', 'blue'}
# print('green' in t)

# pr = {2, 5, 3, 7, 11}
# for i in pr:
#     print(i, end=" ")

# s = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in s if 'a' not in i}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s if i[1] == 'c'}
# print(a)

# a = {0, 1, 2, 3}
# a.add(4)  # добавление элемента
# print(a)
# if 1 in a:
#     a.remove(1)  # если элемента нет, выдает исключение
#
# a.discard(5)  # удаляет элемент, не выдавая исключение
# a.pop()  # удаляет первый элемент, но какой первый? Исключение, если сет пустой
# a.clear()  # очистка множества - остается, но пустое

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b) # c = a | b
# a |= b
# c = a & b # a &= b
# a -= b
# a ^= b
# c = a <= b
# print(a)
# print(c)


# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}

# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print(len(s))
# print("Max =", max(s))
# print("Min =", min(s))

# s1 = "Hello"
# s2 = "How are you"
# s = set(s1) & set(s2)
# print(s)
# for i in s:
#     print(i, end=" ")

# s1 = input("Введите первую строку: ")
# s2 = input("Введите вторую строку: ")
# s = set(s1) - set(s2)
# print(s)

# drawing = {"Марина", "Женя", "Света"}
# music = {"Женя", "Илья"}
#
# only_one_hobby = drawing ^ music
# print("Только одно хобби:", only_one_hobby)
#
# both_hobbies = drawing & music
# print("Два хобби:", both_hobbies)
#
# drawing -= both_hobbies
# print(drawing)

# frozenset
#
# s = frozenset({1, 2, 3, 4, 5})
# print(s)

# Словарь (dict)

# d = {'one': 1, 'two': 2, 'ten': 10, 'one': 11}
# print(d)

# d = {}
# d["one"] = "один"
# d["two"] = "два"
# print(d)

# d1 = dict(one="один", two="два")
# print(d1)

# d = {0: "text1", "one": 45, (1, 2, 3): "кортеж", 42: [2, 3, 6, 7], True: 1}
# print(d)
# print(d[0])
# d["one"] = 100
# print(d)
# d[42][1] += 100
# print(d)

# d = {a: a ** 2 for a in range(7)}
# print(d)

# users = (
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('anna@gmail.com', 'Anna')
# )
#
# print(users)
# d_users = dict(users)
# print(d_users)

# user = (
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('anna@gmail.com', 'Anna')
# )
#
# d_user = dict(user)
# # print('irina@gmail.com' in d_user)
#
# for key in d_user:
#     print(key, "->", d_user[key])

# d = {'one': 1, 'two': 2, 'three': 3}
# key = 'two'
# # if key in d:
# #     del d[key]
#
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом", key, "нет в словаре")
# print(d)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# mult = 1
# for key in d:
#     mult *= d[key]
#
# print(mult)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("Исключить: "))
# del d[dislike]
# print(d)

# d = {'one': 1, 'two': 2, 'three': 3}
# print(len(d))

# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core-i5-4670K", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core-i5-3450", 5, 6400]
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], " руб.",
#           sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         m = int(input("Количество: "))
#         goods[n][1] = m
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], " руб.",
#           sep="")

# Методы словарей

# d = {'one': 1, 'two': 2, 'three': 3}
# print(d['two'])
# value = d.get("two1", "Ключа нет")  # получить значение по (ключ, если ключа нет)
# print(value)
# print(d.keys())  # список ключей
# print(d.items())  # список кортежей (ключ, значение)
# print(d.values())  # список значений
#
# for key, value in d.items():
#     print(key, "=>", value)
#
# d.clear()
# print(d)

# d = {'one': 1, 'two': 2, 'three': 3}
# d2 = d.copy()  # копия словаря
#
# d["four"] = 4
# d2["five"] = 5
#
# print("d", d)
# print("d2", d2)

# d = {'one': 1, 'two': 2, 'three': 3}

# item = d.pop("two")  # удаляет элемент по ключу, возвращает удаляемое значение
# item = d.pop("two", "Ключа нет")
# item = d.setdefault("four", 4)  # добавляет ключ и значение, если ключа нет
# item = d.popitem()  # удаляет произвольную пару и возвращает их в кортеже
# print(item)
# print(d)

# d = {'one': 1, 'two': 2, 'three': 3}
# # d.update({'four': 4, 'five': 5})
# d.update([('four', 4), ('three', 5)])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x.copy()
# z.update(y)
# z = x | y  # объединение словарей в новый словарь
# z = {i: d[i] for d in [x, y] for i in d}
# print(z)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = {}
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# new_d = {'name': d.pop('name'), 'salary': d.pop('salary')}
# print(d)
# print(new_d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d['location'] = d.pop('city')
# print(d)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ": ", a[x][y], sep="")


# sales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3984, "S": 3645, "E": 8821, "W": 2451},
# }
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ": ", sales[x][y], sep="")
#
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person])


# d = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# new_d = {v: k for k, v in d.items()}
# print(new_d)

# d = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# new_d = {k: v for k, v in d.items() if v <= 2}
# print(new_d)

# s = "Hello"
# d = {i: i * 3 for i in s}
# print(d)

# lt = [1, 2, 3, 4]
# # value = input("-> ")
# d = {i: input("-> ") for i in lt}
# print(d)

# d = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# value = list(d.items())
# print(value)

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
#
# print(d)

# zip()

# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
#
# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# f = {k: v for k, v in zip(a, b)}
# print(f)

# d = list(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
#
# d = dict(zip('one', 'two'))
# print(d)

# a = [1, 2, 3]
# print(list(zip(a)))

# print(list(zip(range(5), range(95, 100))))

# a = [1, 2, 3]
# b = {'one', 'two', 'three'}
# c = (4.8, 5.4, 6.7)
# print(tuple(zip(a, b, c)))

# dict_one = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# dict_two = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
#     print(k1, v1)
#     print(k2, v2)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# # print(dict(pairs))
# a, b = zip(*pairs)
# print(a)
# print(b)

# letters = ['b', 'a', 'c', 'd']
# numbers = [3, 2, 1, 4]
# data = list(zip(letters, numbers))
# print(data)
# data.sort()
# print(data)
# data1 = list(zip(numbers, letters ))
# data2 = dict(data1)
# print(data2)
# data3 = sorted(data2.items())
# print(data3)


# one = {'apple': 0.4, 'orange': 0.35, 'pepper': 0.5}
# two = {'pepper': 0.2, 'onion': 0.55}
#
# print({**two, **one})  # распаковка словаря
#
# for k, v in {**two, **one}.items():
#     print(k, "->", v)

# {
#   'apple': 0.4, 'orange': 0.35,
#   'pepper': 0.2, 'onion': 0.55
# }

# data = [2, 5, 3, 4, 1, 5]
# for i in data:
#     print(i, end=" ")
# print()
# for i in range(6):
#     print(i, end=" ")
# print()
# colors = ['red', 'green', 'blue']
# i = 1
# for color in colors:
#     print(i, ") ", color, sep="")
#     i += 1

# colors = ['red', 'green', 'blue']
# for num, val in enumerate(colors, 1):
#     print(num, ") ", val, sep="")

# n = {i: i + 1 for i in range(10, 18)}
# print(n)
#
# for i, (j, v) in enumerate(n.items()):
#     print(i, ": ", j, " -> ", v, sep="")

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)


# def func(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# print(func(2, 3, 4, 5, 1))
# print(func(2, 4, 7))
# print(func())


# def to_dict(*lst):
#     return {i: i for i in lst}
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('gray', (2, 17), 3.11, -4))


# def ch(*args):
#     res = []
#     sr = sum(args) / len(args)
#     print(sr)
#
#     for num in args:
#         if num < sr:
#             res.append(num)
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print((func(1)))
# print((func(1, 2, 3, 'abc')))

# def print_scores(student, *scores):
#     print("Student name:", student)
#     for score in scores:
#         print(score)
#
#
# print_scores("Джонатан", 100, 95, 88, 92, 99)
# print_scores("Роман", 96, 20, 33)

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))

# def db(**data):
#     my_dict.update(data)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# print(my_dict)
#
# def func(aa, *args, d=0, **kwargs):
#     return aa, args, d, kwargs
#
#
# print(func('one', 5, 9, 7, 8, 1, d=6, a=1, b=2, c=3))


# Области видимости

# name = "Tom"  # Глобальная переменная
#
#
# def hi():
#     global name, surname
#     name = "Sam"  # Локальная переменная
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Goodbye", name, surname)
#
#
# print(name)
# hi()
# bye()
# print(name)

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()

# x = 7
#
#
# def add_five(a):
#     x = 2
#
#     def add_two():
#         return a + x
#
#     return add_two()
#
# print(add_five(3))

# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)


# min = [5, 6, 8, 9, 7]
# print(min(min))

#
# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func("world!")


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("a + b =", a + b)
#
#     print("a =", a)
#     fun2(4)
#
#
# fun1()


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("nonlocal:", a)
#
#     inner()
#     t = a
#
#
# fn()
# z = x + t
# print(z)

# def fn1():
#     x = 25
#
#     def fn2():
#         # x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x =', x)
#     fn2()
#     print('fn1.x =', x)
#
#
# fn1()

#
# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add1 = outer(5)
# print(add1(10))
#
# add2 = outer(6)
# print(add2(10))
#
# print(outer(7)(10))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a += 1
#         b += "1"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#
#     def func1():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return func1
#
#
# res1 = func("Москва")
# res1()
# res1()
#
# res2 = func("Сочи")
# res2()
# res2()
#
# res1()


# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make_classifier(lower, upper):
#     def classify_student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return classify_student
#
#
# A = make_classifier(80, 100)
# B = make_classifier(70, 80)
# C = make_classifier(50, 70)
# D = make_classifier(0, 50)
#
# print("A =", A(students))
# print("B =", B(students))
# print("C =", C(students))
# print("D =", D(students))


# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
#


# Лямбда-выражения (анонимная функция)

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
# func = lambda x, y: x + y
#
# print(func(1, 2))
# print(func('a', 'b'))
#
#
# def summa(x, y):
#     return x + y
#
#
# print(summa(1, 2))
# print(summa('a', 'b'))


# print((lambda x, y: x**2 + y**2)(2, 5))


# s = lambda *args: args
#
# print(s(1, 2, 3, 4))
# print(s(10, 20, 30))


# f = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for i in f:
#     print(i('abc_'))


# def inc(n):
#     return lambda x: x + n

# inc = (lambda n: lambda x: x + n)
#
#
# print(inc(42)(1))
# f = inc(42)
# print(f(1))
# print(f(3))


# sum3 = (lambda x: lambda y: lambda z: x + y + z)
# print(sum3(2)(4)(6))


# d = {'b': 10, 'a': 15, 'c': 4}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)


# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6},
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)


# a = [(lambda x, y: x + y), (lambda x, y: x - y),
#      (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[0](15, 5)
# print(b)

# a = {'one': lambda x: x - 1, 'two': lambda x: x + 3, 'three': lambda x: x}
# b = [-3, 10, 0, 2]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))


# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье')
# }
#
# d[4]()


# print((lambda a, b: a if a > b else b)(15, 13))


# print((lambda a, b, c: a if a < b and a < c else b if b < c else c)(9, 8, 5))
# print((lambda a, b, c: min((a, b, c)))(10, -1, 2))


# map(function, iterable)

# def mult(t):
#     return t * 2
#
#
# lst = [1, 8, 12, -5, -10]
#
# lst2 = list(map(mult, lst))
#
# print(lst2)


# print(list(map(lambda t: t * 2,[1, 8, 12, -5, -10])))


# t = (2.88, -1.75, 100.55)
#
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))


# areas = [3.456776, 5.678934, 7.3346554, 45.345343, 78.565325, 1.565654]
# print(list(map(round, areas, range(1, 3))))


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# print(list(map(lambda x, y: (x, y), st, num)))
# print(dict(map(lambda x, y: (x, y), st, num)))


# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda x, y: x + y, l1, l2)))


# filter(func, iterable)

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
#
# print(tuple(filter(lambda s: len(s) == 3, t)))


# b = [66, 90, 68, 59, 76, 60, 80, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)


# import random
#
#
# lst = [random.randint(1, 30) for _ in range(10)]
# lst_new = list(filter(lambda x: 9 < x < 21, lst))
# print(lst)
# print('[10; 20] =', lst_new)

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(m)
# m1 = [x ** 2 for x in range(10) if x % 2]
# print(m1)


# Декоратор

# def hello():
#     return "Hello, I am func 'hello'"
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test())


# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper
#
#
# def func_test():
#     print("Hello, I am a func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def func_wrapper():
#         print('************')
#         func()
#         print('============')
#
#     return func_wrapper
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# @my_decorator
# def bye():
#     print("Hello, I am func 'bye'")
#
#
# func_test()
# bye()


# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())


# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
# @cnt
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
# print_full_name("Ирина", "Ветрова")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study)
#
#
# print_full_name("Ирина", "Елизавета", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def multiply(n1):
#     def mult(fn):
#         def wrap(n2):
#             return n1 * fn(n2)
#
#         return wrap
#     return mult
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
# print(return_num(5))


# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных")
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных")
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello!"):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn("3", "4", "Dog"))
# print(typed_fn2("Hello", "world", "!"))
# # print(typed_fn2(3, 4, 5))
# print(typed_fn3("Hello ", "world ", z=5))


# def args_decorator(tx=None, decorator_text=''):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#
#         return wrap
#
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator
# def hello_world(text):
#     print(text)
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world2(text):
#     print(text)
#
#
# hello_world('Hi!')
# hello_world2('world!')


# print(int("100", 2))
# print(int("100", 8))
# print(int("100", 10))
# print(int("100", 16))

# print(bin(18))  # 0b10010
# print(oct(18))  # 0o22
# print(hex(18))  # 0x12

# print(0b10010, 0o22, 0x12)
# print(0xFF)  # 255


# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)
#
# print(e in "I am learning Python")
# print(e[-1::-1])  # Развернуть строку задом наперед
# e = e[:3] + 't' + e[4:]
# print(e)

# def changeCharToStr(s, c_old, c_new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = changeCharToStr(str1, "и", "!!!!!")
#
# print(str1)
# print(str2)


# print('C:\\program\\file\\')
# print(r'C:\program\file' + "\\")
# print(r'C:\program\file\\'[:-1])

# print(b'a1b2c3')
# print(b'a1b2c3'[1])
# print(b'\xff\xfe\xfd'[1])


# name = "Дмитрий"
# age = "25"
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
#
# print(f"Меня зовут {name}. Мне {age} лет.")

# from math import pi
# print(f"Значение числа pi: {round(pi, 2)}")
# print(f"Значение числа pi: {pi:.2f}")

# x = 10
# y = 5
# print(f"{x = }\n{y = }")
# print(f"{x} x {y} / 2 = {x * y}")

# a = 74
# print(f"{{{{{a}}}}}")
# a = (1, 2, 2)
# print(f"{a}")

# dir_name = "my_doc"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")

# s = """<div>
#     <a href="#">content</a>
# </div>"""
# s1 = '''<div>
#     <a href="#">content</a>
# </div>'''
# print(s)
# print(s1)


# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(max.__doc__)


# import  math as m
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра по заданной высоте и радиусу основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, высота цилиндра
#     """
#     return 2 * m.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)


# print(ord('a'))
# print(ord('#'))
# print(ord('к'))
#
# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# my_str = "Test string for me"
# arr = [ord(x) for x in my_str]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Average:", arr)
# arr += [x for x in [ord(x) for x in (input("-> " + " ")[:6])] if x not in arr]
# print(arr)
#
# if arr[-1] in arr[:-1]:
#     print("Количество последних элементов:", arr.count(arr[-1]) - 1)
#
# arr.sort(reverse=True)
# print(arr)


# print(chr(84))
# print(chr(101))
# print(chr(2977))

# a = 122
# b = 97
# characters = [chr(x) for x in range(min(a, b), max(a, b) + 1)]
# print(*characters)
# print(*(chr(x) for x in range(a, b + 1)) if a < b else
# (chr(x) for x in range(b, a + 1)))

# print("Hello, world!")
#
#
# print('apple' == 'Apple')
# print('apple' > 'Apple')

# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     res = ""
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += random_char
#     return res
#
#
# print("Ваш случайный пароль:", random_password())

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON
#
# print(s.count('o'))  # кол-во вхождений подстроки в строку
# print(s.lower().count('o'))
#
# print(s.find("Python"))  # возвращает 1-й индекс искомой подстроки
#
# print(s.find("Python", -3))
# print(s.index("Python"))

# s = 'один два'
# ind = s.find(' ')
# s = s[ind + 1:] + ' ' + s[:ind]
# print(s)

# s = 'ab12c59p7dq'
# digits = []
# for symbol in s:
#     if '1234567890'.find(symbol) != -1:
#         digits.append(int(symbol))
#
# print(digits)


# s = "hello, WORLD! I am learning Python."
# print(s.rfind("l"))
# print(s.rindex("l"))


# a = "Nearly all web services collect this basic information " \
#     "from users in their server logs. " \
#     "However, Python Tutor does not collect any personally " \
#     "identifiable information from its users."
#
# n = 'N'
#
# if a.count(n) == 1:
#     print(a.find(n))
# elif a.count(n) > 1:
#     print(a.find(n), a.rfind(n))


# s = "I am learning Python, hello, WORLD"
# # ind1 = s.find('h')
# # ind2 = s.rfind('h')
# # res = s[:ind1] + s[ind2 + 1:]
# # print(res)


# s = "hello, WORLD! I am learning Python."
# print(s.startswith("hel"))
# print(s.endswith("n."))


# print('abc123'.isalnum())  # Строка только из букв и цифр?
# print('abc'.isalpha())  # Строка только из букв?
# print('123'.isdigit())  # Строка только из цифр?


# print('py'.center(10, "-"))
# print('py'.center(7, "="))

# print("     py".lstrip())
# print("py        ".rstrip())
# print("     py        ".strip())

# print('https://www.python.org'.lstrip('/:pths'))
# print('py.$$$;'.rstrip(';$.'))
# print('https://www.python.org'.strip('/:pths.org'))
# print('https://www.python.org'.lstrip('/:pths').rstrip('.org'))


# str1 = "Я изучаю Nython. Мне нравится Nython. " \
#        "Nython очень интересный язык программирования."
# print(str1.replace("Nython", "Python", 2))  # Заменяет вхождения


# s = "-"
# seq = ('a', 'b', 'c')
# print(s.join(seq))
# print("..".join(['1', '99']))
# print(":".join("Hello"))  # объединяет итерируемую пос-ть в стр через разделитель

# print("Строка разделенная пробелами".split())
# print('www.python.org.ru'.split(".", 2))
# print('www.python.org.ru'.rsplit(".", 2))


# a = input("-> ").split()
# print(a)
# a = list(map(int, a))
# print(a)


# s = "В строке заменить пробелы звездочками"
# s = s.split()
# s = "*".join(s)
# print(s)

# s = input('FIO: ').split()
# print(f'{s[0]} {s[1][0]}. {s[2][0]}.')


# Регулярные выражения

# import re

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'\.'
# print(re.findall(reg, s))  # возвращает список со всеми совпадениями
# print(re.search(reg, s))  # данные по первому совпадению с шаблоном
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# print(re.match(reg, s))  # поиск по заданному шаблону в начале строки

# print(re.split(reg, s, 1))  # разбивает строку на список подстрок

# print(re.sub(reg, "!", s))  # поиск и замена
#
# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'2[0-9][0-9][0-9]'
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'[^0-9]'
# print(re.findall(reg, s))
#
# s1 = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45." \
#      "Минуты в диапазоне от 00 до 59. 2021-06-15T01:09."
# r1 = '[0-2][0-9]:[0-5][0-9]'
# print(re.findall(r1, s1))


# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# # reg = r'20*'
# # print(re.findall(reg, s))
#
# # d = "Цифры: 7, +17, -42, 0013, 0.3"
# # print(re.findall(r'[+-]?[\d.]+', d))
#
# d = "05-03-1987 # Дата рождения"
#
# print("Дата рождения:", re.sub('#.*', '', d))
# print("Дата рождения:", re.sub('-', '.', re.sub('#.*', '', d)))


# d = 'author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831'
# # r1 = r'\w+\s*=\s*\w+\s*[\w.]*'
# r1 = r'\w+\s*=[^;]+'
# print(re.findall(r1, d))


# s1 = "12 сентября 2023 года"
# r1 = r"\d{4}"
# print(re.findall(r1, s1))

# s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'\w+\.$'
#
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# text = "hello world"
# print(re.findall(r'\w\+', text, re.DEBUG))

# reg = "я"
# print(re.findall(reg, s, re.I))

# text = """
# one
# two
# """
# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))
# print(re.findall(r"one.\w+", text, re.DOTALL))

# print(re.findall("""
# [\w-]+  # part1
# @       # @
# [\w-]+  # part2
# """, "test@mail.ru", re.VERBOSE))


# text = """
# Python,
# python,
# PYTHON
# """
#
# reg = "(?mi)^python"
# print(re.findall(reg, text))

# def validate_name(name):
# return re.findall('^[\w-]{3,16}$', name)
#     return re.search('^[\w-]{3,16}$', name).group()
#
#
# print(validate_name('Python_master'))
# print(validate_name('Pyt'))
#
# s1 = "12345@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru," \
#        "login.3-67@i.ru, 1login@ru.name.ru"
# # r1 = r"[\w.-]+@\w*\.?\w*\.?\w*"
# r1 = r"[\w.-]+@[\w.-]+[\w{2,3}]"
#
# print(re.findall(r1, s1))


# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?o>', text))


# t = "<p>Изображение <img alt='картинка' src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img.*?>'
# reg = r'<img\s+[^>]*?src\s*=\s*[^>]+>'
# print(re.findall(reg, t))


# t = "Петр, Ольга и Виталий отлично учатся"
# reg = "Петр|Ольга"
# print(re.findall(reg, t))

# t = "int = 4, float = 4.0, double = 8.0f"
# reg = r"int\s*=\s*\d+[\w.]*|double\s*=\s*\d+[\w.]*"
# reg = r"(?:int|double)\s*=\s*\d+[\w.]*"
# reg = r"((int|double)\s*=\s*(\d+[\w.]*))"

# print(re.findall(reg, t))


# def validate_name(name):
#     return re.findall(r'^[a-z\d@_-]{6,18}$', name, re.IGNORECASE)
#
#
# print(validate_name('my-p@ssw0rd'))


# s1 = '127.0.0.1'
# reg = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(reg, s1))


# s1 = "Word2016, PS6, AI5"
# reg = r'([a-z]+)(\d+)'
# print(re.findall(reg, s1, re.I))

#
# s1 = "5 + 7*2 -4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s1))


# a = '28-08-2021'
# reg = r'^(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-(19\d\d|20\d\d)$'
# print(re.findall(reg, a))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group(1))
# print(re.findall(reg, s))
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])


# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
#
# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"


# print(re.sub(r'\s*(\w+)\s*', repl_find, text))


# s = "<p>Изображения <img src='bg.jpg'> - фон страницы</p>"
# # reg = r"<img\s+[^>]*src=(['\"])(.*)\1>"
# reg = r"<img\s+[^>]*src=(?P<q>['\"])(.*)(?P=q)>"
# print(re.findall(reg, s)[0][1])
#
# # (?P<name>) (?P=name)


# s = "Самолет прилетает 10/23/2023. Будем вас рады видеть после 10/24/2023."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))


# s = "yandex.com and yandex.ru"
# reg = r'(([a-z0-9\-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r"http://\1", s))


# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("->", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, "=> lst[0]: ", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst[0]: ", lst[0])
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# Конвертировать числа по другим основаниям
# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(255, 16))


# Проверка номера телефона
# def validate_phone(number):
#     reg = r'^\+?7\s*\(?\d{3}\)?\s*[\d\s-]{7,9}$'
#     return re.search(reg, number).group()
#
# print(validate_phone('+7 499 456-45-78'))
# print(validate_phone('+74994564578'))
# print(validate_phone('7 (499) 456 45 78'))
# print(validate_phone('7 (499) 456-45-78'))


# Рекурсия по вложенному списку
# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'],
#          'Alex', ['Bea', 'Bill'], 'Ann']


# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))


# def count_items2(item_list):
#     count = 0
#     for name in item_list:
#         if isinstance((name, str)):
#             count += 1
#         elif isinstance(name, lst):
#             for i in name:
#                 if isinstance(n, str):
#                     count += 1
#                 elif isinstance(n, list):
#                     count += len(n)
#     print(count)


# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'],
#          'Alex', ['Bea', 'Bill'], 'Ann']
#
#
# def count_items(item_list):
#     count = 0
#     stack = []
#     current_list = item_list
#     i = 0
#     while True:
#         if i == len(current_list):
#             if current_list == item_list:
#                 return count
#             else:
#                 current_list, i = stack.pop()
#                 i += 1
#         if isinstance(current_list[i], list):
#             stack.append([current_list, i])
#             current_list = current_list[i]
#             i = 0
#         count += 1
#         i += 1
#
# print(count_items(names))


# Выпрямление списка
# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'],
#          'Alex', ['Bea', 'Bill'], 'Ann']
# 
# def union(s):
#     if not s:
#         return s
#     if isinstance(s[0], list):
#         return union(s[0] + union(s[1:]))
#     return s[:1] + union(s[1:])
# 
# 
# print(union(names))


# Удаляем побелы рекурсией
# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove(" Hello\tWorld! "))


# Линейный (последовательный) поиск


# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# lst = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]
# print(seq_search(lst, 20))
# print(seq_search(lst, 28))


# def seq_search(s, item):
#     pos = 0
#     found = False
#     stop = False
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos] > item:
#                 stop = True
#             else:
#                 pos += 1
#     return found
#
#
# lst = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]
# lst.sort()
# print(lst)
# print(seq_search(lst, 20))
# print(seq_search(lst, 28))


# Бинарный поиск

# def binary_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#
#     return found


# lst = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
# print(binary_search(lst, 93))
# print(binary_search(lst, 28))


# Алгоритмы сортировки
# Пузырьковая сортировка


# from random import randint
# import time


# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array [j + 1], array[j]
#
#
# a = [randint(1, 100) for i in range (10)]
# print(a)
# bubble(a)
# print(a)

# def binary_search(s, item):
#     found = False
#     first = 0
#     last = len(s) - 1
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#                 found = True
#         else:
#             if item < s[midpoint]:
#                     last = midpoint - 1
#             else:
#                     first = midpoint + 1
#
#     return found
#
#
# a = [randint(1, 100) for i in range(10)]
# a.sort()
# print(a)
# n = int(input("Введите число: "))
# if binary_search(a, n):
#     print(f'Число {n} в списке присутствует')
# else:
#     print(f'Число {n} в списке отсутствует')


# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# a = [randint(1, 100) for i in range(10000)]
# start = time.monotonic()
# bubble(a)
# res = time.monotonic() - start
# print(round(res, 3), "sec")

# Сортировка слиянием
# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#     left = merge_sort(a[:n // 2])
#     right = merge_sort(a[n // 2:n])
#
#     i = j = 0
#     res = []
#
#     while i < len(left) or j < len(right):
#         if not i < len(left):
#             res.append(right[j])
#             j += 1
#         elif not j < len(right):
#             res.append(left[i])
#             i += 1
#         elif left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#     return res
#
#
# array = [randint(1, 100) for i in range(10000)]
# start = time.monotonic()
# array = merge_sort(array)
# res = time.monotonic() - start
# print(round(res, 3), "sec")

# Сортировка Шелла
# def shell_sort(s):
#     gap = len(s)
#
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos-gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#         gap //= 2
#     return s
#
#
#
# a = [randint(1, 100) for i in range(10000)]
# start = time.monotonic()
# shell_sort(a)
# res = time.monotonic() - start
# print(round(res, 3), "sec")


# def quick_sort(a):
#     if len(a) > 1:
#         x = a[(len(a) - 1) // 2]
#         low = [i for i in a if i < x]
#         eq = [i for i in a if i == x]
#         high = [i for i in a if i > x]
#         a = quick_sort(low) + eq + quick_sort(high)
#     return a
#
#
# lst = [randint(1, 100) for i in range(10000)]
# start = time.monotonic()
# lst = quick_sort(lst)
# res = time.monotonic() - start
# print(res, "sec")


# lst = [randint(1, 100) for i in range(10000)]
# start = time.monotonic()
# lst.sort()
# res = time.monotonic() - start
# print(res, "sec")


# Работа с файлами

# f = open('text.txt')
# print(f.read(3))
# print(f.read())
# f.close()


# f = open('test.txt')
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# f.close()

#
# f = open('test.txt')
# print(f.readlines())
# f.close()


# f = open('test.txt')
# for line in f:
#     print(line)
# f.close()

# lines = 0
# f = open('test.txt')
#
# print(lines)
# f.close()

# f = open('xyz.txt', 'a')
# f.write("Hello\nworld!")
# f.close()

# f = open('xyz.txt', 'w')
# # lines = ['This is line 1', 'This is line 2']
# lines = [str(i ** 5) for i in range(1, 20)]
# print(lines)
# for index in lines:
#     f.write(index + "\t")
# f.close()


# f = open('text2.txt', 'w')
# f.write("Замена строки в текстовом файле:\nизменить строку в списке;\n"
#         "записать список файл.")
# f.close()
#
# f = open('text2.txt', 'r')
# read_f = f.readlines()
# print(read_f)
# f.close()
# for i in range(len(read_f)):
#     if read_f[i] == "изменить строку в списке;\n":
#         read_f[i] = "Hello world!\n"
# print(read_f)
# f.close()
#
# f = open('text2.txt', 'w')
# f.writelines(read_f)
# f.close()


# f = open("text.txt")
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()


# f = open("text.txt", "r+")
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()


# with open('text3.txt', 'w+') as f:
#     print(f.write('0123456789'))


# f = open('text2.txt', 'w')
# f.write("Работа с файлами реализуется как правило с применением файловых систем, "
#         "обеспечивающих организацию работы с файлами и абстракцию над носителями "
#         "информации.")
# f.close()
# def longest_word(file):
#     with open(file) as text:
#         w = text.read().split()
#         max_length = max(w, key=len)
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# file_name = "text2.txt"
# print(longest_word(file_name))


# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\n" \
#        "Строка №7\nСтрока №8\nСтрока №9\nСтрока №10"
#
# with open('one.txt', 'w') as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
# with open(read_file, 'r') as fr, open(write_file. 'w') as fw:
#     for line in fr:
#         lime = line.replace("Строка", "Линия - ")
#         fw.write(line)

import os
import os.path
import time

# print(os.getcwd())  # возвращает путь к текущей директории
# print(os.listdir())  # возвращает папки и файлы в текущей директории
#
# os.mkdir("folder")  # создает директорию по указанному

# os.makedirs("nested1/nested2/nested3")  # создает конечную и промежуточные папки

# os.rename('nested1', 'test')  # переименование папки

# os.rename("text.txt", "test/text1.txt")
# os.renames("text1.txt", "text/text.txt")  # создаются промежуточные директории

# for root, dirs, files in os.walk("test", topdown=True):  # topdown=True - сверху вниз
#     print("Root:", root)
#     print("Sub_dirs:", dirs)
#     print("Files:", files)

# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print("-" * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#     print("-" * 50)
#
# remove_empty_dirs("test")


# os.path

# print(os.path.split(r'C:\Python\test\nested2\xyz.txt'))  # Разбивает путь на кортеж
# print(os.path.dirname(r'C:\Python\test\nested2\xyz.txt'))  # Имя директории
# print(os.path.basename(r'C:\Python\test\nested2\xyz.txt'))  # Имя файла


# print(os.path.join('C:\Python', 'test', 'xyz.txt'))

# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         # print(file_path)
#         open(file_path, 'w').close()
#
#
# file_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt'
#                   r'Work\F2\F21\f212.txt']
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f'some sample text for {file} file')
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, fl in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(fl)
#     print('-' * 50)
#
# print_tree('Work', topdown=False)
# print_tree('Work', True)


# print(os.path.exists(r'C:\Python\test\nested2\xyz.txt'))  # True, если есть

# path = r'C:\Python\venv\Scripts\python.exe'
# k_size = os.path.getsize(path)  # размер файла
# print(k_size // 1024)
# print(os.path.getmtime(path))  # время последнего изменения файла
# print(os.path.getatime(path))  # время последнего доступа к файлу
# t = os.path.getctime(path)  # время создания файла
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(t)))

# Существует ли файл и где находится
# file_path = r"test\nested2\test.txt"

# if os.path.exists(file_path):
#     dirs, name = os.path.split(file_path)
#     atime = os.path.getatime(file_path)
#     print(f'{name} ({dirs}) - last access time '
#           f'{time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime))}')
#
# else:
#     print(f"File {file_path} doesn't exist!")

# print(os.path.isfile(file_path))  # True, если это файл
# print(os.path.isdir(file_path))  # True, если это директория


# path = r'C:\Python\test'
# obj = os.listdir(path)
# print(obj)
# for i in obj:
#     p = os.path.join(path, i)
#     if os.path.isfile(p):
#         print(f'{i} - file - {os.path.getsize(p)} bytes')
#     elif os.path.isdir(p):
#         print(f'{i} - dir')


# ООП (объектно-ориентированное программирование)

# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#
# print(dir(Point))
# print(Point.__doc__)


# class Point:
#     x = 1
#     y = 1


# p1 = Point()
# p1.x = 410
# p1.y = 200
# Point.y = 100
# print(p1.x, p1.y)
# print(p1.__dict__)
# print(type(p1))
# print(isinstance(p1, Point))

# p2 = Point()
# print(p2.x, p2.y)
#
# print(id(Point))
# print(id(p1))
# print(id(p2))


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
#
# p1.set_coord(5, 10)
# Point.set_coord(p1, 8, 12)
#
# p2 = Point()
# p2.x = 20
# p2.y = 30
#
# p2.set_coord(20, 30)


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\n"
#               f"Номер телефона: {self.phone}\nСтрана: {self.country}\n"
#               f"Город: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва",
#               "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("Анна")
# print(h1.get_name())


# class Car:
#     model = None
#     year = None
#     name_pr = None
#     power = None
#     color = None
#     price = None
#
#     def input_data(self, m, y, name, p, c, pr):
#         self.model = m
#         self.year = y
#         self.name_pr = name
#         self.power = p
#         self.color = c
#         self.price = pr
#
#     def output_data(self):
#         print('Название модели ', self.model)
#         print('Год выпуска ', self.year)
#         print('Производитель ', self.name_pr)
#         print('Мощность двигателя ', self.power, 'л.с')
#         print('Цвет машины ', self.color)
#         print('Цена ', self.price)
#
#     def get_model(self):
#         return self.model
#
#     def set_model(self, value):
#         self.model = value
#
# BMW = Car()
# BMW.input_data('x7 M501', 2021, 'BMW', 530, 'white', 1000)
# BMW.output_data()
# BMW.set_model('Y7')
# print(BMW.output_data())


# class Person:
#     skill = 10
#     # name = ""
#     # surname = ""
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print(f"Иницализатор {self.name} {self.surname}")
#
#     def __del__(self):
#         print("Удаление экземпляра\n")
#     def print_info(self):
#         print("Данные о сотруднике:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print(f"Квалификация сотрудника: {self.name}", self.skill, "\n")
#
#
# p1 = Person('Viktor', 'Reznik')
# p1.print_info()
# p1.add_skill(3)
# del p1
#
# p2 = Person("Anna", "Dolgih")
# p2.print_info()
# p2.add_skill(2)


# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# print(p1.count)
# p2 = Point(15, 20)
# print(p2.count)
# p3 = Point(23, 39)
# print(p3.count)
# print("count =", Point.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f"Инициализация {self.name}")
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# del droid1
# del droid2
# print("Численность роботов:", Robot.k)

# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):  # установить координаты
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else: print("Координаты должны быть числами")
#
#     def get_coord(self):  # получить координаты
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print(f"Координата x должна быть числом")
#     def get_x(self):
#         return self.__x
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print(f"Координата y должна быть числом")
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, '10')
# print(p1.get_coord())
# p1.set_coord(1.5, 7)
# print(p1.get_coord())
# p1.set_x(8)
# p1.set_y(16)
# print(p1.get_coord())
# print(p1.get_x())
# print(p1.get_y())
# print(p1.__dict__)
# p1._Point__x = 111
# print(p1.__dict__)


# class Point:
#     __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):  # установить координаты
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else: print("Координаты должны быть числами")
#
#     def get_coord(self):  # получить координаты
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print(f"Координата x должна быть числом")
#     def get_x(self):
#         return self.__x
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print(f"Координата y должна быть числом")
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
#     def __get_x(self):
#         print("Вызов __get")
#         return self.__x
#
#     def __set_x(self, x):
#         print("Вызов __set")
#         self.__x = x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         print("Вызов __get")
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         print("Вызов __set")
#         self.__x = x
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x

# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x


# class KgToPoinds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPoinds(12)
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "фунтов")
# weight.kg = 41
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "фунтов")

# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, new_old):
#         self.__old = new_old
#
#     @old.deleter
#     def old (self):
#         del self.__old
#
# p1 = Person("Irina", 26)
# p1.name = "Igor"
# p1.age = 31
# print(p1.name)


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))

# class Count:
#     @staticmethod
#     def maxim(a, b, c, d):
#         return max(a, b, c, d)
#
#     @staticmethod
#     def minim(a, b, c, d):
#         return min(a, b, c, d)
#
#     @staticmethod
#     def avg(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def fact(a):
#         factorial = 1
#         for i in range(1, a + 1):
#             factorial *= i
#         return factorial
#
#
# print(Count.maxim(3, 5, 7, 9))
# print(Count.minim(3, 5, 7, 9))
# print(Count.avg(3, 5, 7, 9))
# print(Count.fact(5))

# import math
#
#
# class Area:
#     count = 0
#
#     @staticmethod
#     def triangle_area(a, b, c):
#         p = (a + b + c) / 2
#         Area.count += 1
#         return math.sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def triangle_area2(a, h):
#         Area.count += 1
#         return 0.5 * a * h
#
#     @staticmethod
#     def get_count():
#         return Area.count
#
#     @staticmethod
#     def square_area(a):
#         Area.count += 1
#         return a ** 2
#
#     @staticmethod
#     def rect_area(a, b):
#         Area.count += 1
#         return a * b
#
#
# print(f"Площадь треугольника по формуле Герона:", Area.triangle_area(3, 4, 5))
# print(f"Площадь треугольника через основание и высоту:", Area.triangle_area2(6, 7))
# print(f"Площадь квадрата:", Area.square_area(7))
# print(f"Площадь прямоугольника:", Area.rect_area(2, 6))
# print(f"Количество подсчетов площади:", Area.get_count())


# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))
#         return cls(day, month, year)
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# dates = [
#     '30.12.2020',
#     '30-12-2020',
#     '89.12.2021',
#     '12.03.2022'
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         string_to_db = date.string_to_db()
#         print(string_to_db)

# string_date = "23.10.2021"
# day, month, year = map(int, string_date.split("."))
# date = Date.from_string("23.10.2021")
# print(date.string_to_db())
#
# date2 = Date.from_string("15.11.2021")
# print(date2.string_to_db())


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет №{self.num}, принадлежащий {self.surname}, был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num}, принадлежащий {self.surname}, был закрыт.")
#
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def print_balance(self):
#         print(f"Текущий баланс: {self.value} {Account.suffix}")
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_pecents(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению, у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#
# acc = Account(num='12345', surname='Долгих', percent=0.03, value=1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# acc.add_pecents()
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# acc.withdraw_money(3000)

# import re
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#
#         self.fio = fio
#         self.old = old
#         self.passport = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall(r'[а-яё-]', fio, re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно указать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 18 or old > 90:
#             raise TypeError("Возраст должен быть целым числом от 18 до 90")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат номера паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def passport(self):
#         return self.__passport
#
#     @passport.setter
#     def passport(self, ps):
#         self.verify_ps(ps)
#         self.__passport = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# p1.fio = "Соболев Игорь Николаевич"

# Наследование

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# # print(issubclass(Point, object))
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         print("Инициализатор базового класса Prop")
#         self._sp = sp
#         self._ep = ep
#         self.color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициализитор Line")
#         Prop.__init__(self, *args)
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self.color}, {self.width}")
#
#
# # class Rect(Prop):
# #
# #     def draw_rect(self):
# #         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self.color}, {self.width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()

# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     def area(self):
#         print("Площадь: ", end="")
#         return self.__width * self.__height
#
#     def print_info(self):
#         print(f"Прямоугольник\nШирина: {self.__width}\nВысота: {self.__height}\n"
#               f"Цвет: {self.color}")
#
#
# rect = Rectangle(10, 20, "зеленый")
# rect.color = "синий"
# rect.print_info()
# print(rect.area())

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, (int)) and isinstance(self.__y, (int)):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color},"
#               f"{self._width}")
#
#     def set_coord(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep},"
#               f"{self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(10, 20), Point(100, 200))
# line.draw_line()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.set_coord(Point(30, 40), Point(300, 400))
# rect.draw_rect()


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         super().__init__(width, height)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка:", self.border)
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# shape2 = RectFon(600, 300, "1px solid red")
# shape2.show_rect()


# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))


# Перегрузка методов

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, (int)) and isinstance(self.__y, (int)):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, "
#               f"{self._width}")
#
#     def set_coord(self, sp, ep=None):
#         # super().set_coord(sp, ep)
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print("Координаты должны быть числами")
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть числами")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(10, 20), Point(100, 200))
# line.draw_line()
# line.set_coord(Point(-10, -20))
# line.draw_line()


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, (int)) and isinstance(self.__y, (int)):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть"
#                                   "определн метод draw")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, "
#               f"{self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, "
#               f"{self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, "
#               f"{self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()

# Абстрактный метод
# Асбтрактный класс

# from abc import ABC, abstractmethod


# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на е2")
#
#
# q = Queen()
# q.draw()
# q.move()

# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен "
#                                   "метод calc_area")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.calc_area())
# t = SqTable(20)
# print(t.calc_area())
# t1 = RoundTable(radius=20)
# print(t1.calc_area())


# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=' ')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=' ')
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=' ')
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
#
# for elem in d:
#     elem.print_value()
#     print(f"= {elem.convert_to_rub():.2f} RUB")
#
# for elem in e:
#     elem.print_value()
#     print(f"= {elem.convert_to_rub():.2f} RUB")


# Интерфейс

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child")
#
#
# class Grandchild(Child):
#     def display2(self):
#         print("Grandchild")
#
#
# gc = Grandchild()
# gc.display2()
# gc.display1()


# Вложенные классы

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print("Метод внешнего класса")
#
#     def outer_obj_method(self):
#         print("Обычный метод")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Метод внутреннего класса", MyOuter.age, self.obj.name)
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter('внешний')
# inner = out.MyInner('внутренний', out)
# print(out.name)
# print(inner.inner_name)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "Light green"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()
# print(outer.name)
# print(g.name)


# class Intern:
#     def __init__(self):
#         self.name = "Intern"
#
#     def display(self):
#         print("Name:", self.name)
#
#
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = "Head"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d2 = outer.head
#
# d1.display()
# d2.display()


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.Notebook()
#
#     def show(self):
#         print(self.name, end=" ")
#         self.note.show()
#
#     class Notebook:
#         def __init__(self):
#             self.brand = "HP"
#             self.cpu = "i7"
#             self.ram = 16
#
#         def show(self):
#             print(f" => {self.brand}, {self.cpu}, {self.ram}")
#
#
# s1 = Student("Roman")
# s2 = Student("Vladimir")
#
# s1.show()
# s2.show()


# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("Outer")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("Inner")
#
#         class InnerClass:
#
#             def show(self):
#                 print("InnerClass")
#
#
# out = Outer()
# out.show()
#
# inner1 = out.inner
# inner1.show()
#
# inner2 = inner1.inner_inner  # inner2 = out.inner.inner_inner
# inner2.show()


# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print("In Base Class")
#
#     class Inner:
#         def display1(self):
#             print("Inner if Base Class")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("In SubClass")
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print("Inner of SubClass")
#
#
# a = SubClass()
# a.display()
#
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()


# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")


# class Pet(Creature):
#     def play(self):
#         print(self.name +  " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# beast = Dog("Buddy")
# beast.bark()
# beast.sleep()
# beast.play()


# class A:
#     def __init__(self):
#         print("A")
#
#     def hi(self):
#         print("A_hi")
#
#
# class AA:
#     def __init__(self):
#         print("AA")
#
#     def hi(self):
#         print("AA_hi")
#
#
# class B(A):
#     def __init__(self):
#         print("B")
#
#     def hi(self):
#         print("B_hi")
#
#
# class C(AA):
#     def __init__(self):
#         print("C")
#
#     def hi(self):
#         print("C_hi")
#
#
# class D(B, C):
#     def __init__(self):
#         super().__init__()
#         C.__init__(self)
#         print("D")
#
#     def hi(self):
#         C.hi(self)
#
#
# d = D()
# d.hi()
# print(D.mro())
# print(D.__mro__)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Иницализатор Styles")
#         self.color = color
#         self.width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Инициализатор Pos")
#         self.sp = sp
#         self.ep = ep
#         Styles.__init__(self, *args)
#
#
# class Line(Pos, Styles):
#     # def __init__(self, sp: Point, ep: Point, color="red", width=1):
#     #     Pos.__init__(self, sp, ep)
#     #     Styles.__init__(self, color, width)
#
#     def draw(self):
#         print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()


# Миксин (примеси)
# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggedMixin:
#     def log(self, message, filename="logfile.txt"):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggedMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, filename="log.txt")
#
#
# sub = MySubClass()
# sub.display("Эта строка будет отображаться и записываться в файл")


# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         self.ID += 1
#         self.id = self.ID
#
#     def save_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_log()

# Перегрузка операторов

# Число секунд в одном дне: 24*60*60 = 86400

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return self.sec == other.sec
# #
# #
# c1 = Clock(100)
# c2 = Clock(100)
# if c1 == c2:
#     print("Время равно")
# else:
#     print("Время разное")

# c4 = Clock(300)
# c3 = c1 + c2 + c4
# c2 += c1
# print(c1.get_format_time())
# print(c2.get_format_time())
# print(c3.get_format_time())


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым неотрицательным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Сергей", (5, 5, 3, 4, 5))
# # print(s1.marks[2])
# print(s1[2])
# s1[10] = 5
# del s1[2]
# print(s1.marks)


# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return self.sec == other.sec
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         elif item == "min":
#             return (self.sec // 60) % 60
#         elif item == "sec":
#             return self.sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         if key == "min":
#             self.sec = s + 60 * value + h * 3600
#         if key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# print(c1["hour"], c1["min"], c1["sec"])
# c1["hour"] = 10
# c1["min"] = 61
# c1["sec"] = 30
# print(c1["hour"], c1["min"], c1["sec"])
# print(c1.get_format_time())

# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is a good boy!"
#         elif self.pol == "F":
#             return f"{self.name} is a good girl!"
#         else:
#             return f"{self.name} is a good kitty!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}'"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(["M", "F"])) for i in range(randint(1, 3))]
#         else:
#             raise TypeError("Types are not supported")
#
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elsa", 5, "F")
# cat3 = Cat("Murzik", 3, "M")
# print(cat1)
# print(cat2)
# print(cat1 + cat2)

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())
# if isinstance(g, Rectangle):
#     print(g.get_per_rect())
# else:
#     print(g.get_per_sq())


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text("Python")
# print(t1.total(35))
# print(t2.total(35))


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}."
#
#     def make_sound(self):
#         return f"{self.name} мяукает"
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я собака. Меня зовут {self.name}. Мой возраст {self.age}."
#
#     def make_sound(self):
#         return f"{self.name} гавкает"
#
#
# cat1 = Cat("Пушок", 2.5)
# dog1 = Dog("Мухтар", 4)
#
# animal = [cat1, dog1]
#
# for i in animal:
#     print(i.info())
#     print(i.make_sound())

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)


# class Point:
#     def __init__(self, *args):
#         self.coord = args
#
#     def __len__(self):
#         return len(self.coord)
#
#
# p = Point(1, 2, 2)
# print(len(p))


# class Human:
#     def __init__(self, last_name, first_name, age):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.age = age
#
#     def info(self):
#         print(f"\n{self.last_name} {self.first_name} {self.age}", end=" ")
#
#
# class Student(Human):
#     def __init__(self, last_name, first_name, age, speciality, group, rating):
#         self.specialty = speciality
#         self.group = group
#         self.rating = rating
#         super().__init__(last_name, first_name, age)
#
#     def info(self):
#         super().info()
#         print(f"{self.specialty} {self.group} {self.rating}", end=" ")
#
#
# class Teacher(Human):
#     def __init__(self, last_name, first_name, age, speciality, experience):
#         self.specialty = speciality
#         self.experience = experience
#         super().__init__(last_name, first_name, age)
#
#     def info(self):
#         super().info()
#         print(f"{self.specialty} {self.experience}", end="")
#
#
# class Graduate(Student):
#     def __init__(self, last_name, first_name, age, speciality, group, rating, topic):
#         super().__init__(last_name, first_name, age, speciality, group, rating)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f"{self.topic}", end="")
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in group:
#     i.info()

# import math
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# pt = Point(1, 2)
# print(pt.length)

# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# pt2 = Point2D(1, 2)
# print(pt2.__dict__)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z'
#
#
# pt = Point(1, 2)
# pt3 = Point3D(10, 20)
# pt3.z = 30
# print(pt3.z)


# Функторы

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()


# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(self.__chars)
#
#
# s1 = StripChars("?:!.; ")
# print(s1(" ?Hello World! "))
#
#
# def strip_chars(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(chars)
#
#     return wrap
#
#
# s2 = strip_chars("?:!.; ")
# print(s2(" ?Hello World! "))


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print("*" * 20)
#         self.func()
#         print("*" * 20)
# @MyDecorator
# def func1():
#     print("func")
#
#
# func1()


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         res = self.func(a, b)
#         star = "*" * 20
#         return f"{star}\n{res}\n{star}"
#
#
# @MyDecorator
# def func1(a, b):
#     return a * b
#
#
# @MyDecorator
# def func2(a, b):
#     return a / b
#
#
# print(func1(2, 5))
# print(func2(6, 3))


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         res = self.func(a, b)
#         return res ** 2
#
# @Power
# def mult(a, b):
#     return a * b
#
# print(mult(2, 3))


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         res = self.func(*args, **kwargs)
#         star = "*" * 20
#         return f"{star}\n{res}\n{star}"
#
#
# @MyDecorator
# def func1(a, b):
#     return a * b
#
#
# @MyDecorator
# def func2(a, b, c):
#     return a * b * c
#
#
# print(func1(2, 5))
# print(func2(6, 3, 2))


# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             print("*" * 20)
#             print(self.name)
#             func(a, b)
#             print("*" * 20)
#
#         return wrap
#
#
# @MyDecorator("test")
# def func1(a, b):
#     print(a, b)
#
#
# func1(2, 5)

# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             return func(a, b) ** self.arg
#
#         return wrap
#
#
# @Power(3)
# def mult(a, b):
#     return a * b
#
#
# print(mult(2, 2))


# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()

# def decorator(cls):
#     class Wrap(cls):
#         def double(self, value):
#             return value * 2
#
#     return Wrap
#
#
# @decorator
# class Actual:
#     def __init__(self):
#         print("Иницализатор класса Actual")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = Actual()
#
# print(obj.quad(4))
# print(obj.double(4))


# Дескриптор
# __get__()
# __set__()
# __delete__()
# __set_name__()

# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise TypeError(f"{value} должно быть строкой")
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     self.__surname = value
#
#
# p = Person("Иван", "Петров")
# p.name.set("Владимир")
# print(p.name.get())


# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         print("__get__")
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Иван", "Петров")
# p.surname = "Иванов"
# print(p.name)
# print(p.__dict__)


# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError('Значение должно быть положительным')
#         instance.__dict__[self.name] = value
#
#
# class Order:
#     price = NonNegative()
#     quantity = NonNegative()
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple = Order('apple', 5, 10)
# print(apple.total())


# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f"Координата {coord} должна быть целым числом")
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# p1.x = 5
# print(p1.x)
# print(p1.__dict__)


# from car import electrocar
#
# def run():
#     car1 = electrocar.ElectroCar('Tesla', 'T', 2018, 9000)
#     car1.show_car()
#     car1.description_battery()
#
#
# if __name__ == '__main__':
#     run()


# Упаковка (сериализация) / распаковка (десериализация) данных

# pickle
# json


# import pickle

# file_name = 'basket.txt'
#
# shop_list = {
#     'фрукты': ['яблоки', 'манго'],
#     'овощи': 'морковь',
#     'бюджет': 1000
# }
#
# with open(file_name, 'wb') as fh:
#     pickle.dump(shop_list, fh)
#
# with open(file_name, 'rb') as fh:
#     shop_list2 = pickle.load(fh)
# print(shop_list2)


# class Test:
#     num = 35
#     st = 'привет'
#     lst = [1, 2, 3]
#     d = {'first': 'a', 'second': 2}
#     tpl = (22, 25)
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}\n" \
#                f"Словарь: {Test.d}\nКортеж: {Test.tpl}"
#
#
# obj = Test()
#
# my_obj = pickle.dumps(obj)
# print(my_obj)
#
# my_obj2 = pickle.loads(my_obj)
# print(my_obj2)

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)


# import json

# data = {
#     'name': 'Olga',
#     'age': 35,
#     '20': None,
#     'True': 1,
#     'hobbies': ('running', 'singing'),
#     'children': [
#         {
#             'firstname': 'Alice',
#             'age': 6
#         }
#     ]
# }

# with open('data.json', 'w') as fw:
#     json.dump(data, fw, indent=4)
#
# with open('data.json', 'r') as fw:
#     data1 = json.load(fw)
# print(data1)

# json_string = json.dumps(data, sort_keys=True)
# print(json_string)
# print(json_string[10:14])
#
# data2 = json.loads(json_string)
# print(data2)


# x = {
#     'name': 'Виктор'
# }
# y = {
#     'name': 'Виктор'
# }
#
#
# a = json.dumps(x)
# print(a)
# print(json.loads(a))
#
# print(json.dumps(x, ensure_ascii=False))


# import json
# from random import choice
#
# def gen_person():  # Домашка
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('person.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('person.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())


# class Student:  # косячиный
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ', '.join(map(str, self.marks))
#         return f"Студент: {self.name}: {a}"
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_marks(self):
#         return sum(self.marks) / len(self.marks)
#
#     @staticmethod
#     def dump_to_json(stud, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#
#         data.append({'name': stud.name, 'marks': stud.marks})
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def load_from_file(filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = ''
#         for i in self.students:
#             a += str(i) + "\n"
#         return f"Группа: {self.group}\n{a}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     def dump_group(self, file):
#         with open(file, 'w') as f:
#             stud_list = []
#             for i in self.students:
#                 stud_list.append([i.name, i.marks])
#             json.dump(stud_list, f, indent=2)
#                 # print([i.name, i.marks])
#
#     @staticmethod
#     def upload_journal(file):
#         with open(file) as f:
#             print(json.load(f))
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
# file1 = 'student.json'
# file2 = 'group.json'
# # Student.dump_to_json(st1, file1)
# # Student.dump_to_json(st2, file1)
# # Student.load_from_file(file1)
# sts = [st1, st2]
# my_group = Group(sts, 'ГК Python')
# # print(my_group)
# my_group.add_student(st3)
# # print(my_group)
# my_group.remove_student(1)
# # print(my_group)
# group22 = [st2]
# my_group2 = Group(group22, 'ГК Web')
# Group.upload_journal(file2)
# print(my_group)
# print(my_group2)
# Group.change_group(my_group, my_group2, 0)
# print(my_group)
# print(my_group2)

# print(st1)
# st1.add_mark(4)
# print(st1)
# st1.delete_mark(2)
# print(st1)
# st1.edit_mark(4, 5)
# print(st1)
# print(st1.average_marks())

# import requests
# import json

# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# # print(type(response.text))
# # print(response.text)
# todos = json.loads(response.text)
# # print(todos)
#
# todos_by_user = {}
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
# print(todos_by_user)
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# print(users)
#
# max_users = " and ".join(users)
# print(max_users)
# s = "s" if len(users) > 1 else ""
# print(f"User{s} {max_users} completed {max_complete} todos")
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_complete and has_max_count
#
#
# with open('filtered.json', 'w') as f:
#     filtered_todos = list(filter(keep, todos))
#     json.dump(filtered_todos, f, indent=2)


# CSV (Comma Separated Values)

import csv

# with open('data.csv') as f:
#     file_reader = csv.reader(f, delimiter=";")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {row}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1
#     print(f"Всего в файле {count} строки.")


# with open('data.csv') as f:
#     file_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=";", fieldnames=file_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"\t{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
#         count += 1

# with open('student.csv', 'w') as f:
#     write = csv.writer(f, delimiter=';', lineterminator='\r')
#     write.writerow(['Имя', 'Класс', 'Возраст'])
#     write.writerow(['Женя', '9', '15'])
#     write.writerow(['Саша', '5', '12'])
#     write.writerow(['Маша', '11', '18'])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('sw_data.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
# with open('sw_data.csv') as f:
#     print(f.read())


# with open('stud_1.csv', 'w') as f:
#     name = ['Имя', 'Возраст']
#     file_writer = csv.DictWriter(f, delimiter=';', lineterminator='\r',
#                                  fieldnames=name)
#     file_writer.writeheader()
#     file_writer.writerow({'Имя': 'Саша', 'Возраст': '6'})
#     file_writer.writerow({'Имя': 'Маша', 'Возраст': '15'})
#     file_writer.writerow({'Имя': 'Вова', 'Возраст': '14'})


# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dict_writer.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r',
#                                   fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)


# Парсинг данных с сайта
# pip install beautifulsoup4 или bs4

from bs4 import BeautifulSoup

# f = open('Index.html').read()
# soup = BeautifulSoup(f, 'html.parser')
# # row = soup.find_all("div", class_="row")[2]
# # row = soup.find("div", class_="name")
# # row = soup.find_all("div", class_="row")[1].find("div", class_="links")
# # row = soup.find_all("div", class_="links")[1]
# # row = soup.find_all('div', {"data-set": "salary"})
# # row = soup.find('div', string="Alena").parent.parent
# # row = soup.find('div', string="Alena").find_parent(class_="row")
# row = soup.find('div', id="whois3").find_previous_sibling()
# print(row)


# def get_copywriter(tag):
#     whois = tag.find('div', class_='whois').text
#     if "Copywriter" in whois:
#         return tag
#     return None
# 
# 
# f = open('Index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, 'html.parser')
# copywriter = []
# row = soup.find_all('div', class_='row')
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)

# import re
#
#
# def get_salary(s):
#     pattern = r'\d+'
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('Index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find_all('div', {"data-set": "salary"})
# for i in row:
#     get_salary(i.text)


# import requests
# from bs4 import BeautifulSoup
# import re
# import csv


# res = requests.get('https://ru.wordpress.org/')
# # print(res.status_code)
# # print(res.headers['content-type'])
# print(res.content)
# print(res.text)

# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def refined(s):
#     return re.sub(r"\D", "", s)
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer = csv.writer(f, delimiter=';', lineterminator='\r')
#
#         writer.writerow(data['name'], data['url'], data['rating'])
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all('section', class_='plugin-section')[1]
#     plugins = p1.find_all('article')
#
#     for plugin in plugins:
#         name = plugin.find('h3').text
#         # url = plugin.find('h3').find("a").get('href')
#         url = plugin.find('h3').find("a")['href']
#         rating = plugin.find("span", class_="rating-count").find('a').text
#         r = refined(rating)
#         data = {'name': name, "url": url, 'rating': r}
#         print(data)
#
# def main():
#     url = 'https://ru.wordpress.org/plugins/'
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import csv
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open('plugins1.csv', 'a', encoding='utf-8-sig') as f:
#         writer = csv.writer(f, delimiter=';', lineterminator='\r')
#         writer.writerow((data['name'], data['url'], data['snippet'], data['active_installs'], data['tests']))
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     element = soup.find_all('article', class_='plugin-card')
#     for el in element:
#         try:
#             name = el.find('h3').text
#         except ValueError:
#             name = ''
#
#         try:
#             url = el.find('h3').find('a')['href']
#         except ValueError:
#             url = ''
#
#         try:
#             snippet = el.find('div', class_='entry-excerpt').text.strip()
#         except ValueError:
#             snippet = ""
#
#         try:
#             active = el.find('span', class_='active-installs').text.strip()
#         except ValueError:
#             active = ""
#
#         try:
#             c = el.find('span', class_='tested-with').text.strip()
#             cy = refine_cy(c)
#         except ValueError:
#             cy = ''
#
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active_installs': active,
#             'tests': cy
#         }
#
#         write_csv(data)
#
#         # print(cy)
#
#
# def main():
#     for i in range(26):
#         url = f'https://ru.wordpress.org/plugins/browse/blocks/page/{i}/'
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# from parse import Parser
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()


# import socket
#
# URLS = {
#     '/': "index page",
#     '/blog': "blog page"
# }
#
#
# def parse_request(request):
#     parsed = request.split()
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != "GET":
#         return 'HTTP/1.1 405 Method Not Allowed\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Page Not Found\n\n', 404
#     return 'HTTP/1/1 200 OK\n\n', 200
#
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Page Not Found</h3>'
#     elif code == 405:
#         return '<h1>405</h1><h3>Method Not Allowed</h3>'
#     return URLS[url]
#
#
# def generate_response(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     body = generate_content(code, url)
#     return (headers + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))
#     server_socket.listen()
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#
#         print(f'Клиент: {addr} => \n{request.decode("utf-8")}\n')
#
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close()
#
#
# if __name__ == '__main__':
#     run()

# import socket
# from view import index, blog
#
# URLS = {
#     '/': "index page",
#     '/blog': "blog page"
# }
#
#
# def parse_request(request):
#     parsed = request.split()
#     print(parsed)
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != "GET":
#         return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Page Not Found!\n\n', 404
#     return 'HTTP/1.1 200 OK!\n\n', 200
#
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Page not found!</h3>'
#     elif code == 405:
#         return '<h1>405</h1><h3>Method not allowed!</h3>'
#     return URLS[url]
#
#
# def generate_response(request):
#     print(request)
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     body = generate_content(code, url)
#     return (headers + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 8000))
#     server_socket.listen()
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#         print(request)
#         print(f"Клиент: {addr} => \n{request.decode('utf-8')}\n")
#
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close()
#
#
# if __name__ == '__main__':
#     run()


# СУБД
# SQL (язык структурированных запросов)
# *.db, *.sqlite, *.sqlite3. *.sdb, *.db2


import sqlite3

# con = sqlite3.connect("profile.db")
# cur = con.cursor()
#
# con.close()
#
# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
#     # cur.execute("""CREATE TABLE IF NOT EXISTS user(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # summa REAL,
#     # date TEXT
#     # )
#     # """)
#     cur.execute("DROP TABLE user")


# with sqlite3.connect('users.db') as con:
#     cur = con.cursor()
    # cur.execute("""CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT '+79090000000',
    # age INTEGER NOT NULL CHECK(age > 0 AND age < 100),
    # email TEXT UNIQUE
    # )""")
    # cur.execute("""
    # ALTER TABLE person
    # RENAME TO person_table;
    # """)
    # cur.execute("""
    # ALTER TABLE person_table
    # ADD COLUMN address TEXT NOT NULL DEFAULT 'addr';
    # """)
    # cur.execute("""
    # ALTER TABLE person_table
    # RENAME COLUMN address TO home_address;
    # """)
    # cur.execute("""
    # ALTER TABLE person_table
    # DROP COLUMN home_address;
    # """)
    # cur.execute("""
    # DROP TABLE person_table;
    # """)


# with sqlite3.connect("db_4.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     SELECT *
#     FROM Ware
#     ORDER BY Price DESC
#     LIMIT 2, 5;
#     """)

    # res = cur.fetchall()
    # print(res)
    # for res in cur:
    #     print(res)

    # res = cur.fetchone()
    # print(res)
    # res2 = cur.fetchmany(2)
    # print(res2)

import sqlite3

# cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000)
# ]
#
# with sqlite3.connect('cars.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )""")
#
#     cur.executescript("""
#         DELETE FROM cars WHERE model LIKE 'B%';
#         UPDATE cars SET price = price + 100
#     """)

    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})

    # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

    # for car in cars:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

    # cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
    # cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
    # cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
    # cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
    # cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")


try:
    con = sqlite3.connect('cars.db')
    cur = con.cursor()
    cur.executescript("""CREATE TABLE IF NOT EXISTS cars(
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    );
    BEGIN;
    INSERT INTO cars VALUES(NULL, 'Renault', 22000);
    UPDATE cars2 SET price = price + 100;
    """)
    con.commit()
except sqlite3.Error as e:
    if con:
        con.rollback()
    print("Ошибка выполнения запроса", e)
finally:
    if con:
        con.close
