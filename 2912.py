# Словарь из двух списков

lst1 = ['red', 'green', 'blue']
lst2 = ['#FF0000', '#008000', '#0000FF']

dict12 = dict(zip(lst1, lst2))
print(dict12)


# Словарь с кубами

# d = {i: i**3 for i in range(1, 11)}
# print(d)

# Три словаря в один
#
# d1 = {1: 10, 2: 20}
# d2 = {3: 30, 4: 40}
# d3 = {5: 50, 6: 60}
# big_d = d1 | d2 | d3
# print(big_d)


# Изменить значение в словаре

# d = {'emp1': {'name': 'John', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 6500}}
# d['emp3']['salary'] = 8500
# for x in d:
#     print(x)
#     for y in d[x]:
#         print(y, ": ", d[x][y], sep="")


# Средний балл студентов

# student = {}
# n = int(input("Количество студентов: "))
# s = 0
#
# for i in range(n):
#     stud_name = input(str(i + 1) + "-й студент: ")
#     score = int(input("Балл: "))
#     student[stud_name] = score
#     s += score
#
# avg = s / n
# print("Средний балл:", round(avg))
#
# for i in student:
#     if student[i] > avg:
#         print(i)


# Два списка в словарь

# lst1 = ['color', 'fruit', 'pet']
# lst2 = ['blue', 'apple', 'dog']
#
# d = dict(zip(lst1, lst2))
# print(d)
