"""
Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:

a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
   К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории
Пример использования.     На входе:

rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

На выходе:

new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc, new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc

"""
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


rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="txt")


#   Принято системой!!!