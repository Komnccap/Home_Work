# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# []
# ○Для дочерних объектов указывайте родительскую директорию.
# ○Для каждого объекта укажите файл это или директория.
# ○Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
import os
import json
import sys
import pickle
import csv


def path_move(root_path):
    dot = '.'
    nums = 0
    nums_2 = 0
    my_pac = []
    mjs = []
    for root, dirs, files in os.walk(root_path):
        for name in files:
            my_pac.append(os.path.join(root, name).partition('employment_8/')[2].split('\\'))
    while nums != len(my_pac):
        print(my_pac[nums])
        while nums_2 != len(my_pac[nums]):
            if dot in my_pac[nums][nums_2]:
                mjs.append(f'{my_pac[nums][nums_2]} - Является файлом, его размер '
                           f'{sys.getsizeof(my_pac[nums][nums_2])} байт(а) и находится в папке {my_pac[nums][nums_2 - 1]}')

            else:
                mjs.append(
                    f'{my_pac[nums][nums_2]} - Является директорией и находится в папке {my_pac[nums][nums_2 - 1]}')
            nums_2 += 1
        nums += 1
        nums_2 -= nums_2
    with open('new_json_list.json', 'w', encoding='utf-8') as j:
        json.dump(mjs, j, ensure_ascii=False)


path_move('C:/Users/murma/PycharmProjects/pythonProject1/Home_work/employment_8/Package')
