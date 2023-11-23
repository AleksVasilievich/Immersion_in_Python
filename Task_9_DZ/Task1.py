'''
1)
Создайте функцию generate_csv_file(file_name, rows),
которая будет генерировать по три случайны числа в каждой строке,
от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:
file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.
2)
Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения
вида ax^2 + bx + c = 0.
Функция принимает три аргумента:
a, b, c (целые числа) - коэффициенты квадратного уравнения.
Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).
3)
Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
Декоратор выполняет следующие действия:
Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения
с помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json.
Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots
в файле results.json будет сохранена информация о параметрах
и результатах вычислений для каждой строки данных из CSV-файла.
Пример:
На входе:

generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==101)

На выходе:
True
True
'''
# 1)

import csv
import random

def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for _ in range(rows):
            data = [random.randint(100, 1000) for _ in range(3)]
            writer.writerow(data)
    print(f'Файл {file_name} успешно создан с {rows} строками данных.')

'''
Эта функция создаст CSV-файл с указанным именем и указанным количеством строк данных, 
в каждой из которых будут три случайных числа в диапазоне от 100 до 1000.
'''
# Пример использования

# generate_csv_file('random_numbers.csv', 500)

# 2)

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2*a)
    else:
        root1 = (-b + (discriminant)**0.5) / (2*a)
        root2 = (-b - (discriminant)**0.5) / (2*a)
        return root1, root2

# Пример использования функции
# print(find_roots(1, -3, 2))  # Выведет (2.0, 1.0)
# print(find_roots(1, 2, 3))   # Выведет None, так как дискриминант отрицателен
# print(find_roots(1, -4, 4))  # Выведет 2.0, так как уравнение имеет один корень

# 3)

import csv
import json
from functools import wraps


def save_to_json(func):
    @wraps(func)
    def wrapper(file_name, *args, **kwargs):
        with open(file_name, newline='') as csvfile:
            data = csv.reader(csvfile)
            results = []
            for row in data:
                a, b, c = map(int, row)
                roots = func(a, b, c)
                result_data = {'a': a, 'b': b, 'c': c, 'roots': roots}
                results.append(result_data)

        with open('results.json', 'w') as jsonfile:
            json.dump(results, jsonfile, indent=4)

    return wrapper

# Теперь можно использовать этот декоратор для обертывания функции find_roots,
# чтобы сохранить результаты в формате JSON. Например:
@save_to_json
def find_roots(a, b, c):
    # код функции find_roots
    pass

# Теперь при вызове функции find_roots результаты будут автоматически сохраняться в файл results.json
# Пример вызова функции с аргументом file_name - имя CSV-файла
find_roots('data.csv')