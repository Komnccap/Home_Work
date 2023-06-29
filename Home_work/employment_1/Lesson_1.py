# Написать программу, которая будет выводить в консоль ёлочку заданной высоты
import random


def task_1():
    el = '^'
    el_plus = el * 2
    num = int(input('Введите высоту ёлки: '))
    space = ' ' * num
    count = 0
    space_count = num

    while count < num:
        print(space + el)
        count += 1
        el += el_plus
        space_count -= 1
        space = ' ' * space_count


# Написать порграмму, которая выодит в консоль таблицу умножения "как на тетрадках"
def task_2():
    hor = 2
    vert_count = 1
    hor_count = 1

    while vert_count != 10:
        if hor_count != 11:
            print(f'{hor} * {hor_count} = ', hor * hor_count)
            hor_count += 1
        elif hor_count == 11:
            hor += 1
            hor_count = 1
            vert_count += 1
        else:
            break

# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c -
# стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами
# не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
def task_3():
    a = int(input('Введите сторону А '))
    b = int(input('Введите сторону B '))
    c = int(input('Введите сторону с '))

    while True:
        if a + b > c or a + c > b or b + c > a:
            print('\nТакой треугольник может существовать')
            if a == b != c or a == c != b or b == c != a:
                print('Это равнобедренный треугольник')
            elif a == b and a == c and b ==c:
                print('Это равносторонний треугольник')
            else:
                print('Это разносторонний треугольник')
            break
        else:
            print('Такого труегольника не существует')
            break

# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
def task_4():
    num = int(input('Введите число '))
    first_num = 2
    MAX_VALUE = 100 * 1000
    MIN_VALUE = -100 * 1000
    CURRENT_VALUE = num <= MAX_VALUE and num >= MIN_VALUE
    count = 0
    find_value = 1
    if CURRENT_VALUE == True:
        while count != num:
            num % first_num
            if num % first_num != 0:
                first_num += 1
                count += 1
                find_value += 1
                if find_value <= 2:
                    print('Число простое')
                    break
            else:
                print('Число составное')
                break
    else:
        print('Введено некоректное значение')





#Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать
# «больше» или «меньше» после каждой попытки.
def task_5():
    num = random.randint(0, 5)
    count = 10
    GAME_OVER = 1
    while True:
        print(f'осталось {count} попыток')
        user_num = int(input('Введите ваше число от 0 до 1000 '))
        if count == GAME_OVER:
            print('\nВЫ ПРОИГРАЛИ')
            break
        elif user_num < num:
            print('БОЛЬШЕ')
            count -= 1
        elif user_num > num:
            print('МЕНЬШЕ')
            count -= 1
        elif user_num == num:
            print('ВЫ ПОБЕДИЛИ!')
            break
        else:
            print('Введено некоректное значение')



#task_1()
#task_2()
#task_3()
task_4()
#task_5()


