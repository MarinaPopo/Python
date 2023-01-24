# Частотность символов

tpl = tuple(input("Введите элементы кортежа без пробелов: "))
print(tpl)
lst = []
for i in tpl:
    if i not in lst:
        print("Количество", i, "=", tpl.count(i))
        lst.append(i)


# Список в кортеж

# lst1 = [1, 2, 3, 3, 2]
# lst2 = [2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]
#
#
# def reverse_lst(lst):
#     lst.reverse()
#     new_lst = []
#     for i in lst:
#         if i not in new_lst:
#             new_lst.append(i)
#     return tuple(new_lst)
#
#
# print(reverse_lst(lst1))
# print(reverse_lst(lst2))

# Поиск элемента в кортеже

# tpl = ('ab', 'abcd', 'cde', 'abc', 'def')
# s = input("Введите искомый элемент: ")
# if s in tpl:
#     print("Есть такой элемент")
# else:
#     print("Нет такого элемента")
