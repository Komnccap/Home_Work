def ask(zag: str, answers: list, count_: int = 5):
    print(f'{zag}')
    while count_:
        user_answer = input('Ваш ответ - ').lower()
        try_ = 1
        if user_answer in answers:
            print('Вы угадали!')
            return try_
        else:
            try_ += 1
            count_ -= 1
            print(f'Неправильно, осталось попыток {count_}')
    return 0
