# 1-ая начальная строка
init_str_1 = "Fdsf fds fa fffff afsdf jjtrjyutrjuy fadsfasdf fasdf asdf"
# 1-ая начальная строка
init_str_2 = "афываыфв афывафыв авыфафвы афвыа ыфа афыва фыва ыфва фыва"

# Вычисляем длину строки
len_str = len(init_str_1)

# Создаём пустую строку
result_str = ''

# Итерируемся по длинне строки
for i in range(len_str):
    if i%2: # Если место чётное
        result_str += init_str_1[i] # Добавляем к результирующей строке элемент исходной строки
    else: # Если место нечётное
        result_str += init_str_2[i] # Добавляем к результирующей строке элемент исходной строки

print(result_str)

