import json
capitals = {}

def add_entry(country, capital):
    try:
        capitals = json.load(open('capitals.json'))
    except FileNotFoundError:
        capitals = {}

    capitals[country] = capital
    with open('capitals.json', 'w') as f:
        json.dump(capitals, f, indent=2)


def delete_entry(country):
    with open('capitals.json', 'r') as f:
        json.dump(capitals, f, indent=2)


choice = int(input("Выбор действия:\n1 - добавление данных\n2 - удаление данных"
                   "\n3 - поиск данных\n4 - редактирование данных\n"
                   "5 - просмотр данных\n6 - завершение работы\nВвод: "))

if choice == 1:
    country = input("Введите название страны с заглавной буквы: ")
    capital = input("Введите название столицы с заглавной буквы: ")
    add_entry(country, capital)
    print("Файл сохранен")
elif choice == 2:
    country = input("Введите страну, которую нужно удалить: ")
    print("Файл сохранен")