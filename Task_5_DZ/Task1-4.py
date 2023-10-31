'''
Решение системы
'''

file_path1 = "C:/Users/User/Documents/example.txt"
file_path2 = '/home/user/data/file'
file_path3 = 'D:/myfile.txt'
file_path4 = 'C:/Projects/project1/code/script.py'
file_path5 = '/home/user/docs/my.file.with.dots.txt'
file_path6 = 'file_in_current_directory.txt'

def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)


print(get_file_info(file_path1))
print(get_file_info(file_path2))
print(get_file_info(file_path3))
print(get_file_info(file_path4))
print(get_file_info(file_path5))
print(get_file_info(file_path6))