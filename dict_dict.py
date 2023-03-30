# Записать словарь словарей в json

import json
from random import choice, randint


def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    person = {
        'name': name,
        'tel': tel
    }
    return person


def write_json(person_dict):
    try:
        data = json.load(open('person.json'))
    except FileNotFoundError:
        data = {}

    data[randint(100, 999)] = person_dict
    with open('person.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())

