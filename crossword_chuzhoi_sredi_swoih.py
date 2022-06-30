from functions import open_dicts, find_anagrams, ask


def main(word1: str, word2: str, dictionary: list) -> list:
    res = []
    for i in word1:
        lst1 = list(word1)
        lst2 = list(word2)
        lst1.remove(i)
        lst2.append(i)
        new_word1 = ''.join(lst1)
        new_word2 = ''.join(lst2)
        new_word1_anagrams = find_anagrams(new_word1, DICT_RU)
        new_word2_anagrams = find_anagrams(new_word2, dictionary)
        if new_word1_anagrams and new_word2_anagrams:
            res.append([new_word1_anagrams, new_word2_anagrams, 'Убрать букву: ' + i])
    return res


if __name__ == '__main__':
    DICT_RU, DICT_RU_FULL = open_dicts()

    print('            Кроссворд "ЧУЖОЙ СРЕДИ СВОИХ"')
    print('Введите два набора букв')
    a = input('Набор букв 1: ').lower()
    b = input('Набор букв 2: ').lower()

    result = main(a, b, DICT_RU)

    if len(result) == 0:
        if ask('Ничего не найдено. Использовать полный список?: '):
            result.extend(main(a, b, DICT_RU_FULL))
    else:
        if ask(f'Мы нашли {len(result)} вариантов. Найти больше слов?'):
            result.extend(main(a, b, DICT_RU_FULL))
    if result:
        print('Окончательные результаты поиска:')
        for x in result:
            print(', '.join(x))
    else:
        print('Извините, но ничего не найдено')
