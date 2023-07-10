from random import choice, randint, shuffle

ALLOWED_SYMBOLS = '&*()+-/?!$#@|'
ALLOWED_LETTERS = 'abcdefghijklmnopqrstuvwxyz0123456789_'
TRANSLATED_LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщыэюя №%'
TRANSLATIONS = (
        [x for x in 'abvgde'] +
        ['yo', 'zh'] +
        [x for x in 'ziyklmnoprstufh'] +
        ['ts', 'ch', 'sh', 'sch', 'y', 'e', 'yu', 'ya', '_', 'n', 'proc']
)
transl_dict = {a: b for a, b in zip(TRANSLATED_LETTERS, TRANSLATIONS)}


def latinize(string):
    """
    """
    new_string = str()
    for char in string.lower():
        if char in ALLOWED_LETTERS:
            new_string += char
        elif char in TRANSLATED_LETTERS:
            new_string += transl_dict[char]
    return new_string.strip('_')


def generate_password(length):
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
