# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.

from user_error import UserNumError, UserNegError, UserFloatError, UserUnknownError


class Task:
    def __init__(self, num):
        if isinstance(num, int) and num > 0:
            self.num = num
            print(f'Ваше число в шестнадцатиричном строковом представлении = {hex(num)}')
        else:
            if isinstance(num, str):
                raise UserNumError(num)
            elif isinstance(num, float):
                raise UserFloatError(num)
            elif num < 0:
                raise UserNegError(num)
            else:
                raise UserUnknownError(num)

# task = Task('A')
# task = Task(1.52)
# task = Task(-1)
# task = Task()
