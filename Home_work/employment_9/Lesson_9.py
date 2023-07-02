import math
import random
import csv

rnd, rnd_2, rnd_3 = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)


def csv_maker():
    st_count = random.randint(100, 1000)
    i = 0
    while i < st_count:
        rd, rd_2, rd_3 = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
        with open('csv_dis_finder.csv', 'a', newline='') as cdf:
            filewriter = csv.writer(cdf, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            # filewriter.writerow(['a', 'b', 'c'])
            filewriter.writerow([rd, rd_2, rd_3])
        i += 1


csv_maker()


def dec_finder(func):
    def wrapper(arg_1, arg_2, arg_3):
        print('Вызов функции:', func.__name__)
        # print(f'Полученные аргументы {arg_1} {arg_2} {arg_3}')
        func(arg_1, arg_2, arg_3)

    return wrapper


with open('csv_dis_finder.csv') as cdf:
    data_reader = csv.reader(cdf)
    for line in data_reader:
        print(line)


@dec_finder
def dis(a, b, c):
    print(f'коэффициенты для уравнения: a = {line[0]}, b = {line[1]}, c = {line[2]} ')
    print(f'ax^2 + bx + c = 0:')
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print(f'x1 = {round(x1, 2)}\nx2 = {round(x2, 2)}')
    elif discr == 0:
        x = -b / (2 * a)
        print(f'x = {round(x, 2)}')
    else:
        print('Корней нет')


dis(int(line[0]), int(line[1]), int(line[2]))
