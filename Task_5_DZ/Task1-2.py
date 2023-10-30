import os

file_path = "C:/Users/User/Documents/example.txt"
def get_file_info(file_str):
    path = os.path.dirname(file_str)
    filename = os.path.splitext(os.path.basename(file_str))[0]
    extension = os.path.splitext(file_str)[1]
    return (path, filename, extension)
    # print(path, filename, extension)


# get_file_info(file_path)
info = get_file_info(file_path)
print(info)
# ('C:/Users/User/Documents', 'example', '.txt')