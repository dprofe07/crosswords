def find_anagrams(word, lst):
    res = []
    for x in lst:
        if is_anagram(x, word):
            res.append(x)
    return res


def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)


def choose(label: str, lst: list, repeat: bool = True) -> int:
    print(f'{label}: ')
    for i, ch in enumerate(lst):
        print(f'{i + 1}. {ch}')
    first = True
    while repeat or first:
        first = False
        a = input('Номер: ')
        try:
            a = int(a)
        except ValueError:
            print('Это не число')
            continue

        if a > len(lst) or a < 1:
            print(f'Число должно быть между 1 и {len(lst)}')
            continue

        return a - 1


def open_dicts():
    with open('dict_ru.txt', encoding='windows-1251') as sl:
        a = sl.read().split('\n')

    with open('dict_full_ru.txt', encoding='windows-1251') as slf:
        b = slf.read().split('\n')
    return set(a), set(b)


def ask(quest: str) -> bool:
    print(quest)
    return input('> ').lower() in ['+', 'y', 'да', 'yes', 'д']
