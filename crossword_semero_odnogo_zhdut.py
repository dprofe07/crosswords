from functions import find_anagrams, is_anagram, choose, open_dicts


def myinput(prompt='', check=lambda i: True):
    while check(a := input(prompt)):
        pass
    return a


def line(s, dictionary: list):
    res = []
    for x in 'йцукенгшщзхъфывапролджэячсмитьбюё':
        try:
            i = s.index(' ')
        except ValueError:
            i = 0
        a_ = s.replace(' ', x)
        y = find_anagrams(a_, dictionary)
        if y:
            for a in range(len(y)):
                y[a] = list(y[a])
                y[a][i] = y[a][i].upper()
                y[a] = ''.join(y[a])
            res.extend(y)
    return check(list(set(res)), s)


def check(r, s):
    res = []
    for x in r.copy():
        if (
                is_anagram(x[:s.find(' ')].lower(), s[:s.find(' ')].lower()) and
                is_anagram(x[s.find(' ') + 1:].lower(), s[s.find(' ') + 1:].lower())
        ):
            res.append(x)
    return res


def word(r1, r2, r3, r4, r5, r6, r7, dictionary):
    res = []
    for a in r1:
        a = ''.join([x for x in a if x.isupper()])
        for b in r2:
            b = ''.join([x for x in b if x.isupper()])
            for c in r3:
                c = ''.join([x for x in c if x.isupper()])
                for d in r4:
                    d = ''.join([x for x in d if x.isupper()])
                    for e in r5:
                        e = ''.join([x for x in e if x.isupper()])
                        for f in r6:
                            f = ''.join([x for x in f if x.isupper()])
                            for g in r7:
                                g = ''.join([x for x in g if x.isupper()])
                                word = (a + b + c + d + e + f + g).lower()
                                if word in dictionary:
                                    res.append(word)
    res = list(set(res))
    return res


def card(dictionary: list):
    s = []
    for i in range(7):
        s.append(myinput(f'{i + 1}: ', lambda i: len(i) != 7))
    r = []
    for i in range(7):
        ri = line(s[i], dictionary)
        print(f'Строка {i}:', ', '.join(ri))
        r.append(ri)
    return r


def writecross(words):
    print(' ***Кроссворд***')
    print('     ' + words[0][0] + '   ' + words[1][0])
    print('    ' + words[2])
    print('     ' + words[0][2] + '   ' + words[1][2])
    print('    ' + words[3])
    print(' ' + words[4][0] + ' ' + words[5][0] + ' ' + words[0][4] + '   ' + words[1][4] + ' ' + words[6][0] + ' ' +
          words[7][0])
    print(words[8] + ' ' + words[9])
    print(' ' + words[4][2] + ' ' + words[5][2] + ' ' + words[0][6] + '   ' + words[1][6] + ' ' + words[6][2] + ' ' +
          words[7][2])
    print(' ' + words[4][3] + ' ' + words[5][3] + '       ' + words[6][3] + ' ' + words[7][3])
    print(' ' + words[4][4] + ' ' + words[5][4] + ' ' + words[10][0] + '   ' + words[11][0] + ' ' + words[6][4] + ' ' +
          words[7][4])
    print(words[12] + ' ' + words[13])
    print(' ' + words[4][6] + ' ' + words[5][6] + ' ' + words[10][2] + '   ' + words[11][2] + ' ' + words[6][6] + ' ' +
          words[7][6])
    print('    ' + words[14])
    print('     ' + words[10][4] + '   ' + words[11][4])
    print('    ' + words[15])
    print('     ' + words[10][6] + '   ' + words[11][6])


if __name__ == '__main__':
    DICT_RU, DICT_RU_FULL = open_dicts()
    print('                  Кроссворд "СЕМЕРО ОДНОГО ЖДУТ"')
    full = choose('Выберите тип поиска (обычно хватает быстрого)', ['Быстрый', 'Полный']) == 1
    if full:
        dct = DICT_RU_FULL
    else:
        dct = DICT_RU
    mode = choose('Выберите режим рыботы программы', ['1 слово', '1 карточка', '1 кроссворд'])
    if mode == 0:
        print('Выбран режим работы: СЛОВО')
        print('Введите все данные буквы. Пустое место обозначьте пробелом')
        mode = myinput('Слово: ', lambda i: len(i) != 7)
        print(', '.join(line(mode, dct)))
    elif mode == 1:
        print('Выбран режим работы: КАРТОЧКА')
        print('Вводите построчно. Пустое место обозначьте пробелом(7 символов на строку, 7 строк)')
        w = word(*card(dct))
        print('Ключевое слово: ' + ', '.join(w))
    elif mode == 2:
        print('Выбран самый сложный режим работы: КРОССВОРД')
        print('Вводите построчно, пустое место обозначьте пробелом')
        words = []
        for i in range(1, 17):
            print(f'---Карточка #{i} ---')
            mode = word(*card(dct))
            print('Ключевое слово: ' + ', '.join(mode))
            words.append(mode)
        writecross(words)
