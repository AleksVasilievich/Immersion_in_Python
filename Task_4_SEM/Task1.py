"""
Задание №1
Погружение в Python | Функции
✔ Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
"""

text = 'sdfghj wertyudfghrty efgh sdfghdffgh'.split()


def shift_text(t):
    shift = len(max(t))
    for i, el in enumerate(sorted(t), 1):
        print(f'{i}. {el:>{shift}}')

shift_text(text)