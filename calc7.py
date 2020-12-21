# # Выбор начальной системы исчесления
# s1 = int(input('Введите начальную систему исчесления (2,8,10,16): '))
# # Выбор конечной системы исчесления
# s2 = int(input('Введите начальную систему исчесления (2,8,10,16): '))
#
# # Символы для 16 системы исчесления
# SYMBOL_16 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
#
#
# def calc_s_to_10(numb: str, s: int):
#     '''Пересчёт из выбранной системы (s) в десятичную'''
#     numb_10 = 0
#     symbol_16 = {items: key for key, items in SYMBOL_16.items()}  # Меняем пары ключ:значение в словаре SYMBOL_16
#     for index, numeral_2 in enumerate(reversed(numb)):
#         if numeral_2 in symbol_16:
#             numeral_2 = symbol_16[numeral_2]
#         numb_10 += int(numeral_2) * s ** index
#     return numb_10
#
#
# def calc_10_to_s(numb: int, s: int):
#     '''Пересчёт из десятичной сиcтемы в выбранную (s)'''
#     numb_s = ''
#     while numb >= s:
#         x = numb // s  # Целая часть от деления
#         o = numb % s  # Остаток от деления
#         if o in SYMBOL_16:
#             o = SYMBOL_16[o]
#         numb_s += str(o)
#         numb = x
#     if numb in SYMBOL_16:
#         numb = SYMBOL_16[numb]
#     numb_s += str(numb)
#     numb_s = ''.join(reversed(numb_s))  # Реверс строки
#     return numb_s
#
#
# # Ввод исходного числа
# numb = input('Введите число: ')
# # Расчёт
# num1 = calc_s_to_10(numb, s1)
# result = calc_10_to_s(num1, s2)
# print(result)

sys = int(input('1 = из 10 в 2, 2 = из 2 в 10, 3 = из 10 в 8, 4 = из 8 в 10, 5 = из 10 в 16, 6 = из 16 в 10 '))

# 1 - из 10 в 2
if sys == 1:
    n = int(input("Число: "))
    b = ''
    while n >= 2:
        o = n % 2  # Остаток от деления
        b = str(o) + b
        n = n // 2
    b = str(n) + b
    print(b)

# 2 - из 2 в 10
if sys == 2:
    n = input("Число: ")
    b = 0
    for index, numeral_2 in enumerate(reversed(n)):
        b += int(numeral_2) * 2 ** index
    print(b)

# 3 - из 10 в 8
if sys == 3:
    n = int(input("Число: "))
    b = ''
    while n >= 8:
        o = n % 8  # Остаток от деления
        b = str(o) + b
        n = n // 8
    b = str(n) + b
    print(b)

# 4 - из 10 в 8
if sys == 4:
    n = input("Число: ")
    b = 0
    for index, numeral_2 in enumerate(reversed(n)):
        b += int(numeral_2) * 8 ** index
    print(b)


# 5 - из 10 в 16
if sys == 5:
    n = int(input("Число: "))
    b = ''
    SYMBOL_16 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while n >= 16:
        o = n % 16  # Остаток от деления
        if o in SYMBOL_16:
            o = SYMBOL_16[o]
        b = str(o) + b
        n = n // 16
    if n in SYMBOL_16:
        n = SYMBOL_16[n]
    b = str(n) + b
    print(b)

# 6 - из 10 в 16
if sys == 6:
    n = input("Число: ")
    b = 0
    SYMBOL_16 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for index, numeral_2 in enumerate(reversed(n)):
        if numeral_2 in SYMBOL_16:
            numeral_2 = SYMBOL_16[numeral_2]
        b += int(numeral_2) * 16 ** index
    print(b)


