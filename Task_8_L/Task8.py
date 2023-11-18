'''
Модуль CSV
Для работы с форматом в Python есть встроенный модуль csv. Для его
использования достаточно импорта в начале файла:
● Чтение CSV
Функция csv.reader принимает на вход файловый дескриптор и построчно читает
информацию.

'''

import csv


with open('biostats.csv', 'r', newline='') as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)
