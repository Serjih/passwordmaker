import random
from src.symbol_groups import groups
from src.symbol_groups import incorrect


def mk_pwd():
    print('Select groups of symbols:')
    print('    l - latin lower case')
    print('    u - latin upper case')
    print('    d - digits')
    print('    o - other symbols')
    print()

    selected_groups = set(input('Input modes in one string: ').lower())

    if '*' in selected_groups:
        selected_groups = set('ludo')

    symbol_set = set()

    for ch in selected_groups:
        if ch in groups:
            symbol_set |= groups[ch]

    min_len, max_len = get_min_max_len()
    random_len = random.choice(range(min_len, max_len + 1))
    password = ''

    for i in range(random_len):
        password += random.choice(list(symbol_set))

    print('Your password:', password)
    print('Length:', random_len)

    save = input('Save password? [y/N] ').lower()

    if save != '' and save != 'n':
        save_pwd(password)


def get_min_max_len():
    try:
        min_len = int(input('Input minimal password length: ').strip())

        if min_len < 0:
            raise ValueError
        elif min_len == 0:
            print('0-length password? For what?')
            return None
    except ValueError:
        print('This value is not a number or this number is negative!')
        return None

    try:
        max_len = int(input('Input maximal password length: ').strip())

        if max_len < min_len:
            print('This number is less then minimal password length!')
            return None
    except ValueError:
        print('This value is not a number!')
        return None

    return min_len, max_len


def save_pwd(password):
    file_name = input('Input file name: ').strip()

    if is_correct(file_name):
        f = open(file_name, 'a')

        for_what = input('For what is this password? (type site name): ').strip()

        print(for_what + ':', password, file=f)

        f.close()


def is_correct(file_name):
    flg = True

    if file_name == '':
        return False

    for ch in incorrect:
        if ch in file_name:
            flg = False
            break

    return flg
