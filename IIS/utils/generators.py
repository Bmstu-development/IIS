from random import choice, shuffle

from .converters import ALLOWED_LETTERS, ALLOWED_SYMBOLS


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
