from random import randint

# Линейный поиск введенного числа в случайном списке

def seq_search(s, item):
    pos = 0
    found = False
    while pos < len(s) and not found:
        if s[pos] == item:
            return f'Число {n} в списке присутствует'
        else:
            pos += 1

    if not found:
        return f'Число {n} в списке отсутствует'



a = [randint(1, 100) for i in range(10)]
print(a)
n = int(input("Введите число: "))
print(seq_search(a, n))


# Удаляем строку из файла по индексу

# f = open('test_remove.txt', 'w')
# f.write("Замена строки в текстовом файле:\nизменить строку в списке;\n"
#         "записать список в файл.")
# f.close()
#
# f = open('test_remove.txt')
# a = f.readlines()
# print(a)
# f.close()
#
#
# def remove_string(pos):
#     a.pop(pos)
#     return a
#
#
# f = open('test_remove.txt', 'w')
# f.writelines(remove_string(1))
# print(a)
# f.close()


# Объединить четыре списка, отсортировать по выбору пользователя, найти значение линейным поиском

# lst1 = [5, 9, 6, 7]
# lst2 = [3, 11, 8]
# lst3 = [2, 4]
# lst4 = [10, 1, 12]
# final_lst = lst1 + lst2 + lst3 + lst4
# print(final_lst)
# print("1 - сортировка по убыванию\n2 - сортировка по убыванию")
# srtd = input("-> ")
#
# if srtd == "1":
#     final_lst.sort(reverse=True)
# elif srtd == "2":
#     final_lst.sort()
#
# print(final_lst)
#
#
# def search_num(lst, num):
#     pos = 0
#     found = False
#     while pos < len(lst) and not found:
#         if lst[pos] == num:
#             return f'Число {n} найдено'
#         else:
#             pos += 1
#
#     if not found:
#         return f'Число {n} не найдено'
#
#
# n = int(input("Введите число: "))
# print(search_num(final_lst, n))
#
