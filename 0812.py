# Линия символов

# n = int(input("Количество символов: "))
# char = input("Тип символа: ")
# print("0 - горизонтальная\n1 - вертикальная")
# line = input("Ориентация линии: ")
# while n > 0:
#     if line == "0":
#         print(char, end="")
#         n -= 1
#     elif line == "1":
#         print(char)
#         n -= 1


# Квадрат

i = 0
while i < 6:
    j = 18
    if i % 2 == 0:
        while j > 0:
            print("+", end="")
            j -= 1
        print("")
    else:
        while j > 0:
            print("-", end="")
            j -= 1
        print("")
    i += 1


# Большее из трех чисел

# n1 = int(input("Первое число: "))
# n2 = int(input("Второе число: "))
# n3 = int(input("Третье число: "))
#
# maxim = n1 if n1 > n2 and n1 > n3 else n2 if n2 > n1 and n2 > n3 else n3
# print(maxim)


# Калькулятор

# print("Выберите операцию:\n1 - \"r\" - унарный минус"
#       "\n2 - \"+\" - сложение"
#       "\n3 - \"-\" - вычитание"
#       "\n4 - \"/\" - деление"
#       "\n5 - \"*\" - умножение"
#       "\n6 - \"%\" - остаток"
#       "\n7 - \"<\" - меньшее"
#       "\n8 - \">\" - большее")
# oper = input("Введите цифру: ")
# num1 = float(input("Введите первое число: "))
# if oper == "1":
#     print(-num1)
# else:
#     num2 = float(input("Введите второе число: "))
#     if num2 == 0 and oper == "4":
#         print("На ноль делить нельзя")
#     elif oper == "2":
#         print(num1 + num2)
#     elif oper == "3":
#         print(num1 - num2)
#     elif oper == "4":
#         print(num1 / num2)
#     elif oper == "5":
#         print(num1 * num2)
#     elif oper == "6":
#         print(num1 % num2)
#     elif oper == "7":
#         print(num1) if num1 < num2 else print(num2)
#     elif oper == "8":
#         print(num1) if num1 > num2 else print(num2)
