# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
def task_1(my_path):
    find_path, *_ = my_path.split('Lesson_5.py')
    *_, find_name = my_path.split('/')
    *_, find_resolution = my_path.split('.')
    my_tuple = (find_path, find_name, find_resolution)
    print(f'{my_tuple}\n{type(my_tuple)}')


#Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем
# в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии
def task_2(name_list, salary_list, award_list):
    for i in range(0, len(name_list)):
        award_list[i], *_ = award_list[i].split('%')
        my_dict = {name_list[i]: int(salary_list[i] + (salary_list[i] * float(award_list[i]) / 100))}
        print(my_dict)
        i += 1


#Создайте функцию генератор чисел Фибоначчи (см. Википедию).
def task_3(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

task_1('C:/Users/murma/OneDrive/Рабочий стол/My_python_code/employment_5/Lesson_5.py')
task_2(['Павел', 'Дмитрий', 'Алексей'], [50_000, 25_000, 11_300], ['10.25', '5', '25.7'])
task_3(print(list(task_3(10))))
