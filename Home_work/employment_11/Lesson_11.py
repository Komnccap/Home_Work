# Решить задания, которые не успели решить на семинаре.
# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц
import numpy as np


class Matrix:
    """Ниже будут производиться работы с матрицами"""

    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def print_matrix(self):
        """______Вывод моей матрицы______"""
        return f'Моя матрица {self.my_matrix}'

    def comparison_matrix(self, other):
        """______Сравнение матриц______"""
        if self.my_matrix == self.my_matrix:
            return 'Матрицы равны'
        else:
            return 'Матрицы не равны'

    def addition_matrix(self, other):
        """______Сложение матриц______"""
        mtx = np.array(self.my_matrix)
        mtx_2 = np.array(self.my_matrix)
        add_matrix = mtx + mtx_2
        return add_matrix

    def multi_matrix(self, other):
        """______Умножение матриц______"""
        mtx = np.array(self.my_matrix)
        mtx_2 = np.array(self.my_matrix)
        mult_matrix = mtx * mtx_2
        return mult_matrix


matrix = Matrix([[1, 1, 1, 1, 1], [7, 7, 7, 7, 7]])
matrix_2 = Matrix([[4, 4, 4, 4, 4], [3, 3, 3, 3, 3]])
mtr = Matrix.comparison_matrix(matrix, matrix_2)
am = Matrix.addition_matrix(matrix, matrix_2)
mm = Matrix.multi_matrix(matrix, matrix_2)

print(Matrix.comparison_matrix.__doc__)
print(mtr)
print(Matrix.print_matrix.__doc__)
print(matrix.print_matrix())
print(matrix_2.print_matrix())
print(Matrix.addition_matrix.__doc__)
print(am)
print(Matrix.multi_matrix.__doc__)
print(mm)
