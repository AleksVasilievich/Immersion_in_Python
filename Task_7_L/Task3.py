import os
from pathlib import Path

# создание
#
# os.makedirs('dir/other_dir/new_os_dir')  # Если файл существует будет ошибка
#
# Path('some_dir/dir/new_path_dir').mkdir(parents=True)     # Если файл существует будет ошибка


# Удаление

# os.rmdir('dir')  # Error
# Path('some_dir').rmdir()   # Error

os.rmdir('dir/other_dir/new_os_dir')
Path('some_dir/dir/new_path_dir').rmdir()


