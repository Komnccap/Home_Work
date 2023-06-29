from datetime import datetime

# 1) В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку
c_t = datetime.now()
if c_t.date() == c_t.date():
    out_date = f'День: {c_t.day}, Месяц: {c_t.month}, Год: {c_t.year}, Время {c_t.hour}:{c_t.minute}'
else:
    print('значения не соответствуют действительности')

