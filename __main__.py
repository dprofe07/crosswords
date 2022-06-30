from cffi.setuptools_ext import execfile

crosswords = {
    'Анаграмный': 'crossword_anagramniy',
    'Чужой среди своих': 'crossword_chuzhoi_sredi_swoih',
    'Двойные стандарты': 'crossword_dvoinie_standarty',
    'Первый встречный': 'crossword_perviy_vstrechniy',
    'Семеро одного ждут': 'crossword_semero_odnogo_zhdut',
    'Встретимся в центре': 'crossword_vstretimsa_v_centre',
    'От А до Я': 'crossword_ot_a_do_ya',
}
if __name__ == '__main__':
    print('Кроссворды. Доступные варианты: ')
    for n, i in enumerate(crosswords.keys()):
        print(f'{n + 1}. {i}')
    a = input('Номер: ')
    a = int(a)
    execfile(f'{crosswords[list(crosswords.keys())[a - 1]]}.py', {'__name__': '__main__'})
