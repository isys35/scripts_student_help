# начальная строка
init_str = "Fdsf fds fa fffff afsdf jjtrjyutrjuy fadsfasdf fasdf asdf"

# Раззбиваем строку (разделитель-пробел)
splited_str = init_str.split(' ')

# Раcполагаем в обратном порядке
splited_str.reverse()

# Собираем строку
result_str = ' '.join(splited_str)

print(result_str)