'''
Из созданных на уроке и в рамках домашнего задания функций,
соберите пакет для работы с файлами.
Создайте файл __init__.py и запишите в него все функции:
save_to_json,
find_roots,
generate_csv_file.
'''

code_to_write = '''
import random
import csv
import json
from functools import wraps


def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(rows):
            data = [random.randint(100, 1000) for _ in range(3)]
            writer.writerow(data)
    # print(f'Файл {file_name} успешно создан с {rows} строками данных.')

def save_to_json(func):
    @wraps(func)
    def wrapper(file_name, *args, **kwargs):
        with open(file_name, newline='') as csv_file:
            data = csv.reader(csv_file)
            results = []
            for row in data:
                a, b, c = map(int, row)
                roots = func(a, b, c)
                result_data = {'a': a, 'b': b, 'c': c, 'roots': roots}
                results.append(result_data)

        with open('results.json', 'w') as jsonfile:
            json.dump(results, jsonfile, indent=4)

    return wrapper


@save_to_json
def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        root1 = (-b + (discriminant) ** 0.5) / (2 * a)
        root2 = (-b - (discriminant) ** 0.5) / (2 * a)
        return root1, root2

'''

with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)


# Решение принято системой