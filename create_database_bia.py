from biathlon.database import create_db, Session
from biathlon.biathlete import Athlete
from biathlon.result_table import ResultTable
from random import randint


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_data(Session())


def _load_data(session):
    biathletes = [
        {'last_name': 'Халили ',
         'first_name': 'Карим',
         'region': 'Москва',
         'points': '571'},
        {'last_name': 'Латыпов ',
         'first_name': 'Эдуард',
         'region': 'Башкортостан',
         'points': '464'},
        {'last_name': 'Серохвостов ',
         'first_name': 'Даниил',
         'region': 'Новосибирская область',
         'points': '442'},
        {'last_name': 'Бабиков ',
         'first_name': 'Антон',
         'region': 'Башкортостан',
         'points': '356'},
        {'last_name': 'Елисеев ',
         'first_name': 'Матвей',
         'region': 'Москва',
         'points': '339'},
    ]
    # lessons_names = ['Математика', 'Программирование', 'Философия',
    #                  'Алгоритмы и структуры данных', 'Линейная алгебра',
    #                  'Статистика', 'Физика']
    # group1 = Group(group_name='MDA-7')
    # group2 = Group(group_name='MDA-9')
    # session.add(group1)
    # session.add(group2)

    # for key, it in enumerate(lessons_names):
    #     lesson = Lesson(lesson_title=it)
    #     lesson.groups.append(group1)
    #     if key % 2 == 0:
    #         lesson.groups.append(group2)
    #     session.add(lesson)
    #
    # faker = Faker('ru_RU')
    # group_list = [group1, group2]
    # session.commit()

    last_name = biathletes[0].get('last_name')
    first_name = biathletes[0].get('first_name')
    lag = 0
    result = ResultTable(last_name, first_name, lag)
    session.add(result)

    for i in range(1, 5):
        last_name = biathletes[i].get('last_name')
        first_name = biathletes[i].get('first_name')
        lag += randint(1, 30)
        result = ResultTable(last_name, first_name, lag)

        session.add(result)
    session.commit()

    for i in range(5):
        last_name = biathletes[i].get('last_name')
        first_name = biathletes[i].get('first_name')
        region = biathletes[i].get('region')
        points = biathletes[i].get('points')
        athlete = Athlete(last_name, first_name, region, points)
        session.add(athlete)

    session.commit()
    session.close()
