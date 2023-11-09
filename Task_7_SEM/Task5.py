import  os
from pathlib import Path


file1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
print(f'{file1 = }\n{file1}')

file2 = Path().cwd() / 'dir' / 'new_file2.txt'
print(f'{file2 = }\n{file2}')