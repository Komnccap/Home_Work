import os
import random

file_counter = 0
content = os.listdir('C:\Python_work\employment_7')
#print(len(content))

while file_counter != len(content):
    file_name = content[file_counter].split('.')
    if file_name[1] == 'txt':
        print(file_name[0])
        rnd = random.randint(10000, 1000000)
        str_num = str(rnd)
        user_name = input('Введите желаемое имя файла: ')
        user_number = int(input('Введите количество цифр в порядковом номере: '))
        file_extension = input('Введите расширение файла: ')
        os.renames(f'{file_name[0]}.txt', f'{user_name}_{str_num[0: user_number]}.{file_extension}')
        file_counter += 1
    else:
        #print(content[file_counter])
        file_counter += 1