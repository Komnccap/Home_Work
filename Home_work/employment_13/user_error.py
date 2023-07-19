class UserError(Exception):
    pass


class UserNumError(UserError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Ошибка связанна с вводом некорректного значения, был введён тип {type(self.value)}'


class UserNegError(UserError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value < 0:
            return f'Ошибка связанна с вводом некорректного значения, было введено отрицательное значение {self.value}'


class UserFloatError(UserError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Ошибка связанна с вводом некорректного значения, нужно ввести int вместо {type(self.value)}'


class UserUnknownError(UserError):
    class UserNegError(UserError):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f'Неизвестная ошибка {self.value}'
