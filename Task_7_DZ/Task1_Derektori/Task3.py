import os

def rename_files(folder_path, desired_name, num_digits, source_ext, target_ext):
    files = os.listdir(folder_path)
    filtered_files = [f for f in files if f.endswith("." + source_ext)]
    filtered_files.sort()  # Сортируем файлы

    for idx, file in enumerate(filtered_files, start=1):
        original_name, extension = os.path.splitext(file)
        new_name = desired_name + str(idx).zfill(num_digits) + "." + target_ext
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
        # print(f"Renamed {file} to {new_name}")
        print(new_name)

# Пример использования:
folder_path = "./test_folder/"
rename_files(folder_path, desired_name="new_file_", num_digits=3, source_ext="doc", target_ext="doc")