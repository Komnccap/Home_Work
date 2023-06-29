# 1) Напишите функцию для траспонирования матрицы
def task_1():
    my_matrix = [['x', 'x', 'x', 'x'], ['o', 'o', 'o', 'o']]
    my_cor_matrix = []
    print(my_matrix)
    count = 0
    while count != len(my_matrix[0]):
        if len(my_cor_matrix) != 2:
            my_cor_matrix.append(my_matrix[0][0])
            my_cor_matrix.append(my_matrix[1][0])
        print(f'{my_cor_matrix}')
        count += 1
# 2) Напишите функцию принимающую на вход только ключевые параметры и возвращающую словрь, где ключ - значение
# переданного аргумента, а значение - имя аргумента. Если ключ не хешируем, используйте его строковое представление.


def task_2(**my_dict):
    print(my_dict)
    my_cor_dict = {}
    for key, value in my_dict.items():
        my_cor_dict[value]=key
    print(my_cor_dict)


task_1()
task_2(one=1, two=2)
