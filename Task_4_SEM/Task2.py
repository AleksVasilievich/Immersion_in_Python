"""
Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""
from audioop import reverse

text = 'fsfd yeyyeueue'

def encode_text(text):
    line = []
    for i in text:
        line.append(ord(i))
    print(sorted(set(line), reverse=True))   # set - убераем дубли (список будет состоять только из уникальных кодов)

encode_text(text)


def encode_text1(text):
    return sorted(set([ord(i) for i in text]), reverse=True)

print(encode_text1(text))