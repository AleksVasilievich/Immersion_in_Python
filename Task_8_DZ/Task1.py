'''
Ваша задача - написать программу, которая принимает на вход директорию
и рекурсивно обходит эту директорию и все вложенные директории.
Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle.
Каждый результат должен содержать следующую информацию:
Путь к файлу или директории: Абсолютный путь к файлу или директории.
Тип объекта: Это файл или директория.
Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах.
Важные детали:
Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
Для файлов сохраните их размер в байтах.
Для директорий, помимо их размера, учтите размер всех файлов и директорий,
находящихся внутри данной директории, и вложенных директорий.
Программа должна использовать рекурсивный обход директорий,
чтобы учесть все вложенные объекты.
Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle.
Форматы файлов должны быть выбираемыми.
Для обхода файловой системы вы можете использовать модуль os.
Вам необходимо написать функцию traverse_directory(directory),
которая будет выполнять обход директории и возвращать результаты в виде списка словарей.
После этого результаты должны быть сохранены в трех различных файлах (JSON, CSV и Pickle)
с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.
'''

import os
import json
import csv
import pickle

def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        total_size = 0
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            total_size += total_size
            file_info = {
                "Path": file_path,
                "Type": "File",
                "Size": file_size
            }
            results.append(file_info)
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            total_dir_size = get_dir_size(dir_path)
            total_size += total_size
            dir_info = {
                "Path": dir_path,
                "Type": "Directory",
                "Size": total_dir_size
            }
            results.append(dir_info)
    return results

def get_dir_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
        for dirname in dirnames:
            total_size += get_dir_size(os.path.join(dirpath, dirname))
    return total_size

def save_results_to_json(results, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(results, json_file, indent=2)

def save_results_to_csv(results, output_file):
    with open(output_file, 'w', newline='') as csv_file:
        fieldnames = ["Path", "Type", "Size"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in results:
            writer.writerow(item)

def save_results_to_pickle(results, output_file):
    with open(output_file, 'wb') as pickle_file:
        pickle.dump(results, pickle_file)

# directory = "/путь/к/директории"  # Замените на свой путь
directory = os.getcwd()


results = traverse_directory(directory)
save_results_to_json(results, "output.json")
save_results_to_csv(results, "output.csv")
save_results_to_pickle(results, "output.pickle")
print(results)


'''
Решение системы ниже !
'''

# import os
# import json
# import csv
# import pickle
#
#
# def get_dir_size(start_path='.'):
#     total_size = 0
#     for dirpath, dirnames, filenames in os.walk(start_path):
#         for f in filenames:
#             fp = os.path.join(dirpath, f)
#             total_size += os.path.getsize(fp)
#         for d in dirnames:
#             dp = os.path.join(dirpath, d)
#             total_size += get_dir_size(dp)
#     return total_size
#
#
# def save_results_to_json(results, file_name):
#     with open(file_name, 'w') as f:
#         json.dump(results, f)
#
#
# def save_results_to_csv(results, file_name):
#     with open(file_name, 'w', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(['Path', 'Type', 'Size'])
#         for result in results:
#             writer.writerow([result['Path'], result['Type'], result['Size']])
#
#
# def save_results_to_pickle(results, file_name):
#     with open(file_name, 'wb') as f:
#         pickle.dump(results, f)
#
#
# def traverse_directory(directory):
#     results = []
#     for root, dirs, files in os.walk(directory):
#         for name in files:
#             path = os.path.join(root, name)
#             size = os.path.getsize(path)
#             results.append({'Path': path, 'Type': 'File', 'Size': size})
#         for name in dirs:
#             path = os.path.join(root, name)
#             size = get_dir_size(path)
#             results.append({'Path': path, 'Type': 'Directory', 'Size': size})
#     return results
