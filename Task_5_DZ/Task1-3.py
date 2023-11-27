
from pathlib import Path

def get_file_info(file_path):
    path = Path(file_path).parent
    filename = Path(file_path).stem
    extension = Path(file_path).suffix
    return (str(path), filename, extension)

file_path = "C:/Users/User/Documents/example.txt"
info = get_file_info(file_path)
print(info)  # ('C:/Users/User/Documents', 'example', '.txt')