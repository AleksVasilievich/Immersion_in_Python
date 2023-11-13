import os

'''
Из созданных на уроке и в рамках домашнего задания функций, 
соберите пакет для работы с файлами
Создайте файл __init__.py и запишите в него функцию rename_files
'''


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


if __name__ == '__main__':
    rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")