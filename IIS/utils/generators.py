from random import choice, shuffle

from .converters import ALLOWED_LETTERS, ALLOWED_SYMBOLS


def generate_password(length):
    """

    :param length:
    :return:
    """
    if length < 8:
        raise ValueError('Password must not be shorter than 8 characters')

    pwd = str()
    for i in range(int(length / 3)):
        pwd += choice(ALLOWED_LETTERS)
        pwd += choice(ALLOWED_LETTERS.upper())
        pwd += choice(2 * ALLOWED_SYMBOLS)
    for i in range(length - len(pwd)):
        pwd += choice(ALLOWED_SYMBOLS)
    pwd_list = list(pwd)
    shuffle(pwd_list)
    return ''.join(pwd_list)


NAMES = []
SURNAMES = []
PATRONYMICS = []
ORGANIZATION = []


def generate_person(number):
    """

    :param number:
    :return:
    """
    from pathlib import Path
    from people.models import Person
    if number < 1:
        raise ValueError('You can not generate less than 1 person')

    names_dir = Path(__file__).resolve().parent.parent
    names = {'f': open(f'{names_dir}/fixtures/data/names_f.txt', 'r').readlines(),
             'm': open(f'{names_dir}/fixtures/data/names_m.txt', 'r').readlines()}
    surnames = {'f': open(f'{names_dir}/fixtures/data/surnames_f.txt', 'r').readlines(),
                'm': open(f'{names_dir}/fixtures/data/surnames_m.txt', 'r').readlines()}
    patronymics = {'f': open(f'{names_dir}/fixtures/data/patronymics_f.txt', 'r').readlines(),
                   'm': open(f'{names_dir}/fixtures/data/patronymics_m.txt', 'r').readlines()}
    organisations = ['МГТУ им. Н. Э. Баумана', 'МГУ', 'НИЯУ МИФИ', 'КриптоПро', 'Эшелон', 'ПромПрогноз', 'Лицей №1580',
                     'Психиатрическая больница №5', 'Наркологический диспансер №498', 'Касперский', 'Яндекс',
                     'Сбербанк', 'Правительство РФ', 'Безработный', 'НИУ ВШЭ']
    sex = ['f', 'm']
    for i in range(number):
        person_sex = choice(sex)
        Person(
            name=choice(names[person_sex]),
            surname=choice(surnames[person_sex]),
            patronymic=choice(patronymics[person_sex]) * choice([0, 1]),
            organisation=choice(organisations),
            bmstu_group='ИУ8-46' * choice([0, 1]),
            phone_number='8(800)555-35-35' * choice([0, 1]),
            tg_username='user_telegram' * choice([0, 1]),
            is_user=bool(choice([0, 1])),
        ).save()
