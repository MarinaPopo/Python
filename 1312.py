a = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
list_pos = []
max_num = a[0]
for i in a:
    if i > 0:
        list_pos.append(i)
    if i > max_num:
        max_num = i
print("Список:", a)
print("Положительный список:", list_pos)
print("Наибольший элемент списка:", max_num)


# a = [int(input("-> ")) for i in range(int(input("Введите элементы списка: ")))]
# k = int(input("Введите индекс: "))
# c = int(input("Введите значение: "))
# a.insert(k, c)
# print(a)


# a = []
# for i in range(1, 11):
#     a.append(i**2)
# print(a)