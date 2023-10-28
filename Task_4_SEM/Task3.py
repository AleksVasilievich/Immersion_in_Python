"""
Задание №3
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""

text = '90 48'

def encode_dist(text):
    lst = sorted([int(i) for i in text.split()])   # два числа
    text_dist = {}
    for el in lst:
        text_dist[chr(el)] = el

    return text_dist

print(encode_dist(text))

def encode_dist1(text):
    lst = sorted(int(i) for i in text.split())
    text_dist = {chr(el): el for el in range(lst[0], lst[1] + 1)}    # диапазон чисел

    return text_dist

print(encode_dist1(text))