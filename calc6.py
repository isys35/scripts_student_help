import csv

# Заголовок
header = ['наименование', 'срок хранения', 'стоимость', 'сорт', 'дата выпуска', 'срок годно- сти']

# Данные
data = [{'наименование': '', 'срок хранения': '', 'стоимость': 0, 'сорт': '', 'дата выпуска': '', 'срок годно- сти': ''},
        {'наименование': '', 'срок хранения': '', 'стоимость': 0, 'сорт': '', 'дата выпуска': '', 'срок годно- сти': ''},
        {'наименование': '', 'срок хранения': '', 'стоимость': 0, 'сорт': '', 'дата выпуска': '', 'срок годно- сти': ''},
        {'наименование': '', 'срок хранения': '', 'стоимость': 0, 'сорт': '', 'дата выпуска': '', 'срок годно- сти': ''},
        {'наименование': '', 'срок хранения': '', 'стоимость': 0, 'сорт': '', 'дата выпуска': '', 'срок годно- сти': ''},
        {'наименование': '', 'срок хранения': '', 'стоимость': 0, 'сорт': '', 'дата выпуска': '', 'срок годно- сти': ''}]

# Окрываем файл
with open('data.csv', "w", newline='') as csv_file:
    # Читаем с помощью модуля csv
    writer = csv.writer(csv_file, delimiter=';')
    # Записываем заголовок
    writer.writerow(header)
    # Записываем данные
    for el in data:
        writer.writerow([el['наименование'],
                         el['срок хранения'],
                         el['стоимость'],
                         el['сорт'],
                         el['дата выпуска'],
                         el['срок годно- сти']])
