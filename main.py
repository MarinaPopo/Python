# name = "Marina"  # создание переменной
# age = 20
# print("Hello,", name)
# print(type(age))

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

x = 10
y = 5
print(f"{x = }\n{y = }")
print(f"{x} x {y} / 2 = {x * y}")

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


