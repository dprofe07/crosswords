from functions import open_dicts, ask


def main(word1: str, word2: str, alphabet: str, dictionary: list) -> list:
    a_s = []
    b_s = []
    all_s = []
    if len(word1) == 4:
        for i in range(4):
            for j in range(i + 1, 4):
                a_s.append(word1[i] + word1[j])
                b_s.append(word2[i] + word2[j])

        for letter in alphabet:
            for a in a_s:
                for b in b_s:
                    all_s.append(a + letter + b)

    elif len(word1) == 6:
        for i in range(6):
            for j in range(i + 1, 6):
                for k in range(j + 1, 6):
                    a_s.append(word1[i] + word1[j] + word1[k])
                    b_s.append(word2[i] + word2[j] + word2[k])

        for letter in alphabet:
            for a in a_s:
                for b in b_s:
                    all_s.append(a + letter + b)

    res = []
    for i in all_s:
        if i in dictionary:
            res.append(i)
    return res


if __name__ == '__main__':
    DICT_RU, DICT_RU_FULL = open_dicts()

    print('               Кроссворд "ВСТРЕТИМСЯ В ЦЕНТРЕ"  ')
    print('Для ускорения поиска вы можете ввести все центральные буквы, которые есть в кроссворде.')
    print('Если вы не хотите использовать эту функцию, просто нажмите Enter')
    alph = input('Введите буквы в кроссворде: ')
    if alph == '':
        print('Вы не используете ускорение поиска')
        ALPHABET = ''.join('йцукенгшщзхъфывапролджэячсмитьбюё')
    else:
        ALPHABET = alph
    w1 = input('Слово 1: ')
    w2 = input("Слово 2: ")
    print('Выполняется поиск:')
    print(f'{w1} + {ALPHABET} + {w2}')

    result = main(w1, w2, ALPHABET, DICT_RU)
    if len(result) == 0:
        if ask('Ничего не найдено. Использовать полный список?'):
            result.extend(main(w1, w2, ALPHABET, DICT_RU_FULL))
    else:
        if ask(f'Найдено {len(result)} вариантов. Найти больше слов?'):
            result.extend(main(w1, w2, ALPHABET, DICT_RU_FULL))
    if result:
        print('Результаты поиска:')
        print(', '.join(set(result)))
    else:
        print('Извините, но ничего не найдено')
