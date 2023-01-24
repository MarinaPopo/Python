# Заменяем все четные символы в строке

def replace_even(s, char):
    str2 = ""
    for i in range(len(s)):
        if i % 2 == 0:
            str2 += char
        else:
            str2 += s[i]
    return str2


str1 = "0123456789"
print(replace_even(str1, "*"))

# Удаляем символ по заданному номеру позиции

# def delete_char(s, pos):
#     return s[:pos] + s[(pos+1):]
#
#
# str1 = "0123456789"
# print(delete_char(str1, 3))


# Удаляем все вхождения заданного символа

# def remove_char(s, char):
#     str2 = ""
#     for i in s:
#         if i != char:
#             str2 += i
#     return str2
#
#
# str1 = "Мама мыла раму"
# print(remove_char(str1, "а"))


# Переводим десятичное число в двоичное

# def to_binary(num):
#     s = ""
#     while num > 0:
#         s += str(num % 2)
#         num = int(num / 2)
#     print(s[-1::-1])
#
#
# x = None
# while x != 0:
#     x = int(input("-> "))
#     to_binary(x)
