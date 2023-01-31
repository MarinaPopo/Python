# Удалить из строки первое и последнее вхождение буквы и все символы между

s = "I am learning Python, hello, WORLD"
ind1 = s.find('h')
ind2 = s.rfind('h')
res = s[:ind1] + s[ind2 + 1:]
print(res)


# Развернуть последовательность символов между первым и последним вхождением буквы

# s = "I am learning Python. hello, WORLD"
# ind1 = s.find('h')
# ind2 = s.rfind('h')
# res = s[:ind1 + 1] + s[ind2 - 1:ind1:-1] + s[ind2:]
# print(res)


# Заменить указанную подстроку. Строку, старую и новую подстроку вводит пользователь.

# s = input("Строка: ")
# old_substring = input("Старая подстрока: ")
# new_substring = input("Новая подстрока: ")
# res = s.replace(old_substring, new_substring)
# print(res)


# Найти количество слов, начинающихся с буквы е

# s = "Ежевику для ежат\nПринесли два ежа.\nЕжевику еле-еле\nЕжата возле ели съели."
# print(s)
# s2 = s.replace("\n", " ")
# print(f"Количество слов: {s2.count('Е') + s2.count(' е')}")

