"""
Задание №2
✔ Самостоятельно сохраните в переменной строку текста.
✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
✔ Напишите преобразование в одну строку.
"""

text = 'abracadabra'
dct = {item: ord(item) for  item in text}

print(dct)