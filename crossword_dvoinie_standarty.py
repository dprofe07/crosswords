from functions import open_dicts, find_anagrams, is_anagram


def main(word1: str, word2: str, dictionary: list) -> None:
    dictionary6 = filter(lambda i: len(i) == 6, dictionary)
    pairs = set()
    for del_word1 in word1:
        for del_word2 in word2:
            res_word1 = word1.replace(del_word1, '', 1) + del_word2
            res_word2 = word2.replace(del_word2, '', 1) + del_word1
            word1_anagrams = find_anagrams(res_word1, dictionary6)
            lst_word2 = find_anagrams(res_word2, dictionary6)
            res1 = []
            for i in word1_anagrams:
                if i.startswith(del_word2):
                    res1.append(i)
            res2 = []
            for i in lst_word2:
                if i.startswith(del_word1):
                    res2.append(i)
            if res1 and res2:
                while len(res1) < len(res2):
                    res1.append(res1[-1])
                while len(res2) < len(res1):
                    res2.append(res2[-1])
                for a, b in zip(res1, res2):
                    pairs.add((a, b))

    print('Нашлись такие пары слов:')
    for i, p in enumerate(pairs):
        print(f'{i + 1}: {p[0]}, {p[1]}')

    print('Сейчас сделаю из них большие слова.')
    for res1, res2 in pairs:
        for start1 in range(3):
            for start2 in range(3):
                lst = find_anagrams(res1[start1:start1 + 4] + res2[start2:start2 + 4], dictionary)
                for i in lst:
                    if is_anagram(i[:4], res1[start1:start1 + 4]) and is_anagram(i[4:], res2[start2: start2 + 4]):
                        print(f'{res1} + {res2} = {lst[0].upper()}')


if __name__ == '__main__':
    DICT_RU = open_dicts()[0]
    DICT6_RU = [i for i in DICT_RU if len(i) == 6]

    print('                  Кроссворд "ДВОЙНЫЕ СТАНДАРТЫ"')
    print('Введите 2 набора букв')
    a = input('1: ')
    b = input('2: ')

    main(a, b, DICT6_RU)
