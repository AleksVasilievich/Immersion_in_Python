"""
Задание №1
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""
import random


def fill_file(file_num, file_name):
    with open(file_name, 'a+', encoding='utf-8') as f:
        for _ in range(0, file_num):
            file_int = random.randint(-1000, 1000)
            file_float = random.uniform(-1000, 1000)
            f.write(f'{file_int} | {file_float:.2f}\n')


filename = "file_txt.txt"
fill_file(file_num=7, file_name=filename)