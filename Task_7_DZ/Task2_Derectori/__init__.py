# from Task2 import rename_files
#
# __all__ = ['rename_files']

import os


def rename_files(desired_name, num_digits, source_ext, target_ext):
    folder_path = "./test_folder/"
    files = os.listdir(folder_path)
    filtered_files = [f for f in files if f.endswith("." + source_ext)]
    file_res = []

    for idx, file in enumerate(filtered_files, start=1):
        original_name, extension = os.path.splitext(file)
        new_name = desired_name + str(idx).zfill(num_digits) + "." + target_ext
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
        file_res.append(new_name)

    print(', '.join(file_res))
    # return  file_res


with open("__init__.py", "r") as init_file:
    code = init_file.read()

function_names = ["def rename_files"]

for func_name in function_names:
    if func_name not in code:
        print(f"Функция {func_name} не найдена в файле __init__.py")
    else:
        print(f"Функция {func_name} найдена в файле __init__.py")
