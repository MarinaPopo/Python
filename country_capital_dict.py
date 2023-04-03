import json

try:
    capitals = json.load(open('capitals.json'))
except FileNotFoundError:
    capitals = {}


def add_entry(cntry, city):
    capitals[cntry] = city
    with open('capitals.json', 'w') as f:
        json.dump(capitals, f, indent=2)
    print("Файл сохранен")


def delete_entry(cntry):
    with open('capitals.json', 'w') as f:
        if cntry in capitals:
            capitals.pop(cntry)
            json.dump(capitals, f, indent=2)
            print("Файл сохранен")
        else:
            print("В файле нет такой страны")


def find_entry(cntry):
    with open('capitals.json') as f:
        if cntry in capitals:
            print(f"Страна: {cntry}, столица: {capitals[cntry]}")
        else:
            print("В файле нет такой страны")


def edit_entry(cntry, city):
    with open('capitals.json', 'w') as f:
        capitals[cntry] = city
        json.dump(capitals, f, indent=2)
        print("Файл сохранен")


while True:
    choice = int(input("Выбор действия:\n1 - добавление данных\n2 - удаление данных"
                       "\n3 - поиск данных\n4 - редактирование данных\n"
                       "5 - просмотр данных\n6 - завершение работы\nВвод: "))
    if choice == 1:
        country = input("Введите название страны с заглавной буквы: ")
        capital = input("Введите название столицы с заглавной буквы: ")
        add_entry(country, capital)
    elif choice == 2:
        country = input("Введите страну, которую нужно удалить: ")
        delete_entry(country)
    elif choice == 3:
        country = input("Введите страну, чтобы узнать столицу: ")
        find_entry(country)
    elif choice == 4:
        country = input("Введите страну, чтобы изменить столицу: ")
        if country in capitals:
            capital = input("Введите новое название столицы: ")
            edit_entry(country, capital)
        else:
            print("В файле нет такой страны")
    elif choice == 5:
        print(capitals)
    elif choice == 6:
        break
    else:
        print("Введите номер действия от 1 до 6")
print("До свидания")
