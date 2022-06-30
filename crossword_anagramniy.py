from functions import find_anagrams, open_dicts, ask


def main(word1: str, word2: str, dictionary: list) -> list:
    return find_anagrams(word1 + word2, dictionary)


if __name__ == '__main__':
    DICT_RU, DICT_RU_FULL = open_dicts()

    print('                  Кроссворд "АНАГРАМНЫЙ"')
    print('Введите два слова, из которых нужно составить одно')
    a = input('Слово 1: ')
    b = input('Слово 2: ')

    res = main(a, b, DICT_RU)

    if res:
        if ask(f'Найдено {len(res)} вариантов. Найти больше?'):
            res.extend(find_anagrams(a+b, DICT_RU_FULL))
    else:
        if ask('Ничего не найдено. Использовать полный список слов?'):
            res.extend(find_anagrams(a+b, DICT_RU_FULL))
    print('Результаты поиска: ')
    print(', '.join(set(res)))
