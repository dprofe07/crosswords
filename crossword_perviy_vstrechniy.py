from functions import open_dicts


def make_word(tbl, *letters):
    w = ''
    for i in range(7):
        w += tbl[letters[i]][i]
    if len(w) != 7:
        return ''
    return w


def del_word(tbl, *letters):
    for i in range(7):
        tbl[letters[i]][i] = ''


def main(tbl: list, dictionary: list) -> list:
    res = []
    for l1 in range(3):
        for l2 in range(3):
            for l3 in range(3):
                for l4 in range(3):
                    for l5 in range(3):
                        for l6 in range(3):
                            for l7 in range(3):
                                word = make_word(tbl, l1, l2, l3, l4, l5, l6, l7)
                                if word in dictionary:
                                    res.append(word)
                                    del_word(tbl, l1, l2, l3, l4, l5, l6, l7)
                                if len(res) >= 2:
                                    break
    return res


if __name__ == '__main__':
    DICT_RU, DICT_RU_FULL = open_dicts()

    print('                  Кроссворд "ПЕРВЫЙ ВСТРЕЧНЫЙ"')
    print('Введите 3 набора букв, образующих таблицу')
    table = [
        [],
        [],
        []
    ]
    for i in range(3):
        table[i].extend(input(str(i + 1) + ': '))

    res = main(table, DICT_RU)

    if len(res) == 2:
        res = ''
        for i in range(7):
            res += table[0][i] or table[1][i] or table[2][i]
        res = ''.join(reversed(res))
        print('Нужное слово читается в другом направлении!')
        print(f'Найдено слово: {res.upper()}')
    else:
        print(f'Найдено слово: {res[0].upper()}')
        print('Оставшиеся слова читаются в другом направлении')
        for i in table:
            i.reverse()
        words = main(res, DICT_RU)

    print('Оставшиеся слова:', ', '.join(res))
