# Начальные данные
initial_data = [3, -2, 3, 5, -4, 1,
                4, 3, 12, -3, 3, 54,
                31, -33, 43, 3, 10]


def calculation(data):
    # Поиск положительных чисел
    positive_numbers = [number for number in data if number >= 0]
    # Поиск отрицательных чисел и вычисление их модуля
    negative_numbers_modulo = [abs(number) for number in data if number < 0]
    s = 0
    n = 1
    for number in positive_numbers:
        # Расчёт произведения положительных чисел
        n *= number
    for number in negative_numbers_modulo:
        # Расчёт суммы отрицательных чисел
        s += number
    # Деление произведения положительных чисел на сумму отрицательных по модулю
    result = n / s
    # Возврат результата
    return result


# Вычиление результата
result = calculation(initial_data)
# Вывод результата
print(result)
