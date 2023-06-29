from fractions import Fraction


def task_1():
    num = int(input('Введите число: '))
    print(f'Ваше число в шестнадцатиричном строковом представлении = {hex(num)}')


def task_2():
    num_1, num_2 = (int(input('Числитель первого числа - ')), int(input('Знаменатель первого числа - ')))
    nums_1 = Fraction(num_1, num_2)
    num_3, num_4 = (int(input('Числитель второго числа - ')), int(input('Знаменатель второго числа - ')))
    nums_2 = Fraction(num_3, num_4)
    print(f'Сумма дробей равна {nums_1 + nums_2} \nпроизведение дробей равно {nums_1 * nums_2} ')


task_1()
task_2()
