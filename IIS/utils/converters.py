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
