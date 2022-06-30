from itertools import product

from functions import choose, open_dicts


def main_vert(word: str, consonants: list, dictionary: set) -> list:
    dct = {
        '1': 'ая',
        '2': 'оэ',
        '3': 'ею',
        '4': 'иуы',
    }
    variants = []
    for i in word:
        variants.append(dct.get(i, i))
    c_index = 0
    for i in range(len(variants)):
        if variants[i] == '.':
            variants[i] = consonants[c_index]
            c_index += 1
    res = []
    prd = product(*variants)
    for i in prd:
        if ''.join(i) in dictionary:
            res.append(''.join(i))
    return list(set(res))


def main_horiz(word: str, consonants: str, dictionary: set) -> list:
    dct = {
        '.': consonants,
        '1': 'ая',
        '2': 'оэ',
        '3': 'ею',
        '4': 'иуы',
    }
    variants = []
    for i in word:
        variants.append(dct.get(i, i))
    res = []
    prd = product(*variants)
    for i in prd:
        if ''.join(i) in dictionary:
            res.append(''.join(i))
    return list(set(res))


if __name__ == '__main__':
    DICT_RU, DICT_RU_FULL = open_dicts()
    print('            Кроссворд "От А до Я"')
    direction = choose('Как распологается слово?', ['По горизонтали', 'По вертикали'])
    if direction == 0:
        print('Введите цвета. Обозначайте:')
        print('1 - зелёный(А, Я)')
        print('2 - синий(О, Э)')
        print('3 - красный(Е, Ю)')
        print('4 - серый(И, У, Ы)')
        print('. - белый(согласная буква)')
        print('Если вы точно знаете, где стоит какая-то буква, можете сразу писать её')
        w = input('Слово: ')
        print('Теперь введите всё оставшиеся в ряду согласные')
        consons = input('Согласные в ряду: ')
        print(', '.join(main_horiz(w, consons, DICT_RU)))
    else:
        print('Введите цвета. Обозначайте:')
        print('1 - зелёный(А, Я)')
        print('2 - синий(О, Э)')
        print('3 - красный(Е, Ю)')
        print('4 - серый(И, У, Ы)')
        print('. - белый(согласная буква)')
        print('Если вы точно знаете, где стоит какая-то буква, можете сразу писать её')
        w = input('Слово: ')
        print('Теперь на каждую введённую точку введите в отдельной строке согласные')
        consons = []
        for i in range(w.count('.')):
            consons.append(input('Согласные: '))
        print(', '.join(main_vert(w, consons, DICT_RU)))