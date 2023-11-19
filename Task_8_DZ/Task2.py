'''
Из созданных на уроке и в рамках домашнего задания функций,
соберите пакет для работы с файлами.
Создайте файл __init__.py и запишите в него все функции:
get_dir_size,
save_results_to_json,
save_results_to_csv,
save_results_to_pickle, traverse_directory.
'''

code_to_write = '''

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
            total_dir_size = calc_total_size(dir_path)
            total_size += total_size
            dir_info = {
                "Path": dir_path,
                "Type": "Directory",
                "Size": total_dir_size
            }
            results.append(dir_info)
    return results

def calc_total_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
        for dirname in dirnames:
            total_size += calc_total_size(os.path.join(dirpath, dirname))
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
'''

with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)


