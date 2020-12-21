# Выбор начальной системы исчесления
s1 = int(input('Введите начальную систему исчесления (2,8,10,16): '))
# Выбор конечной системы исчесления
s2 = int(input('Введите начальную систему исчесления (2,8,10,16): '))

# Символы для 16 системы исчесления
SYMBOL_16 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def calc_s_to_10(numb: str, s: int):
    '''Пересчёт из выбранной системы (s) в десятичную'''
    numb_10 = 0
    symbol_16 = {items: key for key, items in SYMBOL_16.items()}  # Меняем пары ключ:значение в словаре SYMBOL_16
    for index, numeral_2 in enumerate(reversed(numb)):
        if numeral_2 in symbol_16:
            numeral_2 = symbol_16[numeral_2]
        numb_10 += int(numeral_2) * s ** index
    return numb_10


def calc_10_to_s(numb: int, s: int):
    '''Пересчёт из десятичной сиcтемы в выбранную (s)'''
    numb_s = ''
    while numb >= s:
        x = numb // s  # Целая часть от деления
        o = numb % s  # Остаток от деления
        if o in SYMBOL_16:
            o = SYMBOL_16[o]
        numb_s += str(o)
        numb = x
    if numb in SYMBOL_16:
        numb = SYMBOL_16[numb]
    numb_s += str(numb)
    numb_s = ''.join(reversed(numb_s))  # Реверс строки
    return numb_s


# Ввод исходного числа
numb = input('Введите число: ')
# Расчёт
num1 = calc_s_to_10(numb, s1)
result = calc_10_to_s(num1, s2)

print(result)