s1 = int(input('Начальная система исчесления(2,8,10,16): '))
s2 = int(input('Конечная система исчесления(2,8,10,16): '))
s = input('Введите число: ')


def check_10():
    for sym in s:
        if sym not in [str(num) for num in range(10)]:
            print('Число не соответствует выбранной системе исчесления')
            return False
    return True


def check_8():
    for sym in s:
        if sym not in [str(num) for num in range(8)]:
            print('Число не соответствует выбранной системе исчесления')
            return False
    return True


def check_16():
    for sym in s:
        if sym not in [str(num) for num in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']:
            print('Число не соответствует выбранной системе исчесления')
            return False
    return True


def check_2():
    for sym in s:
        if sym not in ['0', '1']:
            print('Число не соответствует выбранной системе исчесления')
            return False
    return True


# из 10 в 2
if s1 == 10 and s2 == 2:
    if check_10():
        n = int(s)
        result = ''
        while n >= 2:
            o = n % 2  # Остаток от деления
            result = str(o) + result
            n = n // 2
        result = str(n) + result
        print(result)

# из 8 в 2
if s1 == 8 and s2 == 2:
    if check_8():
        num_10 = 0
        for index, numeral in enumerate(reversed(s)):
            num_10 += int(numeral) * 8 ** index
        n = num_10
        result = ''
        while n >= 2:
            o = n % 2  # Остаток от деления
            result = str(o) + result
            n = n // 2
        result = str(n) + result
        print(result)

# из 16 в 2
if s1 == 16 and s2 == 2:
    if check_16():
        num_10 = 0
        SYMBOL_16 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        for index, numeral in enumerate(reversed(s)):
            if numeral in SYMBOL_16:
                numeral = SYMBOL_16[numeral]
            num_10 += int(numeral) * 16 ** index
        n = num_10
        result = ''
        while n >= 2:
            o = n % 2  # Остаток от деления
            result = str(o) + result
            n = n // 2
        result = str(n) + result
        print(result)

# из 10 в 8
if s1 == 10 and s2 == 8:
    if check_10():
        n = int(s)
        result = ''
        while n >= 8:
            o = n % 8  # Остаток от деления
            result = str(o) + result
            n = n // 8
        result = str(n) + result
        print(result)

# из 16 в 8
if s1 == 16 and s2 == 8:
    if check_16():
        num_10 = 0
        SYMBOL_16 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        for index, numeral in enumerate(reversed(s)):
            if numeral in SYMBOL_16:
                numeral = SYMBOL_16[numeral]
            num_10 += int(numeral) * 16 ** index
        n = num_10
        result = ''
        while n >= 8:
            o = n % 8  # Остаток от деления
            result = str(o) + result
            n = n // 8
        result = str(n) + result
        print(result)

# из 2 в 8
if s1 == 2 and s2 == 8:
    if check_2():
        num_10 = 0
        for index, numeral in enumerate(reversed(s)):
            num_10 += int(numeral) * 2 ** index
        n = num_10
        result = ''
        while n >= 8:
            o = n % 8  # Остаток от деления
            result = str(o) + result
            n = n // 8
        result = str(n) + result
        print(result)

# из 2 в 16
if s1 == 2 and s2 == 16:
    if check_2():
        num_10 = 0
        for index, numeral in enumerate(reversed(s)):
            num_10 += int(numeral) * 2 ** index
        n = num_10
        result = ''
        SYMBOL_16 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        while n >= 16:
            o = n % 16  # Остаток от деления
            if o in SYMBOL_16:
                o = SYMBOL_16[o]
            result = str(o) + result
            n = n // 16
        if n in SYMBOL_16:
            n = SYMBOL_16[n]
        result = str(n) + result
        print(result)

# из 8 в 16
if s1 == 8 and s2 == 16:
    if check_8():
        num_10 = 0
        for index, numeral in enumerate(reversed(s)):
            num_10 += int(numeral) * 8 ** index
        n = num_10
        result = ''
        SYMBOL_16 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        while n >= 16:
            o = n % 16  # Остаток от деления
            if o in SYMBOL_16:
                o = SYMBOL_16[o]
            result = str(o) + result
            n = n // 16
        if n in SYMBOL_16:
            n = SYMBOL_16[n]
        result = str(n) + result
        print(result)

# из 10 в 16
if s1 == 10 and s2 == 16:
    if check_10():
        n = int(s)
        result = ''
        SYMBOL_16 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        while n >= 16:
            o = n % 16  # Остаток от деления
            if o in SYMBOL_16:
                o = SYMBOL_16[o]
            result = str(o) + result
            n = n // 16
        if n in SYMBOL_16:
            n = SYMBOL_16[n]
        result = str(n) + result
        print(result)

# из 2 в 10
if s1 == 2 and s2 == 10:
    if check_2():
        result = 0
        for index, numeral in enumerate(reversed(s)):
            result += int(numeral) * 2 ** index
        print(result)

# из 8 в 10
if s1 == 8 and s2 == 10:
    if check_8():
        result = 0
        for index, numeral in enumerate(reversed(s)):
            result += int(numeral) * 8 ** index
        print(result)

# из 16 в 10
if s1 == 16 and s2 == 10:
    if check_16():
        result = 0
        SYMBOL_16 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        for index, numeral in enumerate(reversed(s)):
            if numeral in SYMBOL_16:
                numeral = SYMBOL_16[numeral]
            result += int(numeral) * 16 ** index
        print(result)
