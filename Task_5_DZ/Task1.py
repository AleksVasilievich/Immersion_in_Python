'''
Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
Пример использования.
На входе:     file_path = "C:/Users/User/Documents/example.txt"
На выходе:   ('C:/Users/User/Documents/', 'example', '.txt')
'''

# file_path = "C:/Users/User/Documents/example.txt"
file_path = '/home/user/data/file'

def get_file_info(file_path):

    text1 = '.' + ''.join(file_path.split(".")[-1:])
    text2 = (''.join(file_path.split("/")[-1:])).replace(text1, '')
    text3 = (' '.join(file_path.split("/")[:-1])).replace(' ', '/')
    text_set = (text3, text2, text1)
    return text_set


print(get_file_info(file_path))

# print(get_file_info(file_path='C:/Users/User/Documents/example.txt'))