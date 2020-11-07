students = [
    ["0001", "Антонов", "Антон", "Игоревич", "20.08.2009", "БСТ161"],
    ["1102", "Богов", "Артем", "Игоревич", "25.01.2010", "БСТ162"],
    ["0333", "Глаголева", "Анастасия", "Николаевна", "11.07.2009", "БСТ163"],
    ["4004", "Степанова", "Наталья", "Александровна", "13.02.2008", "БСТ161"],
    ["0045", "Боков", "Игорь", "Харитонович", "02.06.2009", "БСТ161"],
    ["0096", "Васильков", "Валентин", "Сергеевич", "20.03.2009", "БСТ164"],
    ["0607", "Сиропова", "Виолетта", "Эдуардовна", "28.05.2010", "БСТ162"]
]

students_dict = {student[0]: student[1:] for student in students}


def change_student_group(student_id, new_group):
    for student_key in students_dict:
        if student_key == student_id:
            students_dict[student_key][-1] = new_group
            break


def fio(group):
    fio_list = []
    for student_id in students_dict:
        if students_dict[student_id][-1] == group:
            fio_list.append(' '.join(students_dict[student_id][:3]))
    print('\n'.join(fio_list))


if __name__ == '__main__':
    print(students)
    print(students_dict)
    print('Студенты группы БСТ161:')
    fio("БСТ161")