# Буквы в первой строке, которых нет во второй

str1 = set(input("Первая строка: "))
str2 = set(input("Вторая строка: "))
str1 -= str2
for i in str1:
    print(i, end=" ")


# Сколько гласных?

# str1 = list(input("Введите строку: "))
# vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
# vowels_count = 0
# for i in str1:
#     if i in vowels:
#         vowels_count += 1
# print("Количество гласных:", vowels_count)


# Все буквы, присутствующие хотя бы в одной строке

# str1 = set(input("Введите первую строку: "))
# str2 = set(input("Введите вторую строку: "))
# str3 = str1 | str2
# print("Буквы:")
# for i in str3:
#     print(i, end=" ")


# Уникальные буквы

# str1 = set(input("Введите первую строку: "))
# str2 = set(input("Введите вторую строку: "))
# str3 = str1 ^ str2
# print("Буквы:")
# for i in str3:
#     print(i, end=" ")