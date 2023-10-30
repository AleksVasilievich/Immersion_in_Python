РМИНАЛ

Не
все
тесты
пройдены, есть
ошибки: (

    Количество затраченных попыток: 4

Время выполнения: 1.376729 сек

Общая статистика
Всего тестов: 6. Пройдено: 0. Не пройдено: 6.

Подробную информацию по каждому тесту смотрите ниже.

Тест 1
Тест не пройден ✗

Формулировка:

* Имя проверяемого метода / функции: get_file_info

* Аргументы, передаваемые в метод / функцию:


file_path = 'C:/Users/User/Documents/example.txt'

* Итоговый код для проверки.Иногда добавляем что-то от себя:)

import warnings

warnings.filterwarnings('ignore')


# При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# file_path = "C:/Users/User/Documents/example.txt"

def get_file_info(file_path):
    text1 = '.' + ''.join(file_path.split(".")[-1:])
    text2 = (''.join(file_path.split("/")[-1:])).replace(text1, '')
    text3 = (' '.join(file_path.split("/")[:-1])).replace(' ', '/')
    text_set = (text3, text2, text1)
    return text_set


print(get_file_info(file_path='C:/Users/User/Documents/example.txt'))

print(get_file_info(file_path='C:/Users/User/Documents/example.txt'))

Ожидаемый
ответ:

('C:/Users/User/Documents/', 'example', '.txt')

Ваш
ответ:

('C:/Users/User/Documents', 'example', '.txt')
('C:/Users/User/Documents', 'example', '.txt')
Тест
2
Тест
не
пройден ✗

Формулировка:

*Имя
проверяемого
метода / функции: get_file_info

*Аргументы, передаваемые
в
метод / функцию:

file_path = '/home/user/data/file'

*Итоговый
код
для
проверки.Иногда
добавляем
что - то
от
себя:)


import warnings

warnings.filterwarnings('ignore')

# При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# file_path = "C:/Users/User/Documents/example.txt"


def get_file_info(file_path):
    text1 = '.' + ''.join(file_path.split(".")[-1:])
    text2 = (''.join(file_path.split("/")[-1:])).replace(text1, '')
    text3 = (' '.join(file_path.split("/")[:-1])).replace(' ', '/')
    text_set = (text3, text2, text1)
    return text_set


print(get_file_info(file_path='C:/Users/User/Documents/example.txt'))

print(get_file_info(file_path='/home/user/data/file'))

Ожидаемый
ответ:

('/home/user/data/', '', '.file')

Ваш
ответ:

('C:/Users/User/Documents', 'example', '.txt')
('/home/user/data', 'file', './home/user/data/file')
Тест
3
Тест
не
пройден ✗

Формулировка:

*Имя
проверяемого
метода / функции: get_file_info

*Аргументы, передаваемые
в
метод / функцию:

file_path = 'D:/myfile.txt'

*Итоговый
код
для
проверки.Иногда
добавляем
что - то
от
себя:)


import warnings

warnings.filterwarnings('ignore')

# При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# file_path = "C:/Users/User/Documents/example.txt"


def get_file_info(file_path):
    text1 = '.' + ''.join(file_path.split(".")[-1:])
    text2 = (''.join(file_path.split("/")[-1:])).replace(text1, '')
    text3 = (' '.join(file_path.split("/")[:-1])).replace(' ', '/')
    text_set = (text3, text2, text1)
    return text_set


print(get_file_info(file_path='C:/Users/User/Documents/example.txt'))

print(get_file_info(file_path='D:/myfile.txt'))

Ожидаемый
ответ:

('D:/', 'myfile', '.txt')

Ваш
ответ:

('C:/Users/User/Documents', 'example', '.txt')
('D:', 'myfile', '.txt')
Тест
4
Тест
не
пройден ✗

Формулировка:

*Имя
проверяемого
метода / функции: get_file_info

*Аргументы, передаваемые
в
метод / функцию:

file_path = 'C:/Projects/project1/code/script.py'

*Итоговый
код
для
проверки.Иногда
добавляем
что - то
от
себя:)


import warnings

warnings.filterwarnings('ignore')

# При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# file_path = "C:/Users/User/Documents/example.txt"


def get_file_info(file_path):
    text1 = '.' + ''.join(file_path.split(".")[-1:])
    text2 = (''.join(file_path.split("/")[-1:])).replace(text1, '')
    text3 = (' '.join(file_path.split("/")[:-1])).replace(' ', '/')
    text_set = (text3, text2, text1)
    return text_set


print(get_file_info(file_path='C:/Users/User/Documents/example.txt'))

print(get_file_info(file_path='C:/Projects/project1/code/script.py'))

Ожидаемый
ответ:

('C:/Projects/project1/code/', 'script', '.py')

Ваш
ответ:

('C:/Users/User/Documents', 'example', '.txt')
('C:/Projects/project1/code', 'script', '.py')
Тест
5
Тест
не
пройден ✗

Формулировка:

*Имя
проверяемого
метода / функции: get_file_info

*Аргументы, передаваемые
в
метод / функцию:

file_path = '/home/user/docs/my.file.with.dots.txt'

*Итоговый
код
для
проверки.Иногда
добавляем
что - то
от
себя:)


import warnings

warnings.filterwarnings('ignore')

# При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# file_path = "C:/Users/User/Documents/example.txt"


def get_file_info(file_path):
    text1 = '.' + ''.join(file_path.split(".")[-1:])
    text2 = (''.join(file_path.split("/")[-1:])).replace(text1, '')
    text3 = (' '.join(file_path.split("/")[:-1])).replace(' ', '/')
    text_set = (text3, text2, text1)
    return text_set


print(get_file_info(file_path='C:/Users/User/Documents/example.txt'))

print(get_file_info(file_path='/home/user/docs/my.file.with.dots.txt'))

Ожидаемый
ответ:

('/home/user/docs/', 'my.file.with.dots', '.txt')

Ваш
ответ:

('C:/Users/User/Documents', 'example', '.txt')
('/home/user/docs', 'my.file.with.dots', '.txt')
Тест
6
Тест
не
пройден ✗

Формулировка:

*Имя
проверяемого
метода / функции: get_file_info

*Аргументы, передаваемые
в
метод / функцию:

file_path = 'file_in_current_directory.txt'

*Итоговый
код
для
проверки.Иногда
добавляем
что - то
от
себя:)


import warnings

warnings.filterwarnings('ignore')

# При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# file_path = "C:/Users/User/Documents/example.txt"


def get_file_info(file_path):
    text1 = '.' + ''.join(file_path.split(".")[-1:])
    text2 = (''.join(file_path.split("/")[-1:])).replace(text1, '')
    text3 = (' '.join(file_path.split("/")[:-1])).replace(' ', '/')
    text_set = (text3, text2, text1)
    return text_set


print(get_file_info(file_path='C:/Users/User/Documents/example.txt'))

print(get_file_info(file_path='file_in_current_directory.txt'))

Ожидаемый
ответ:

('', 'file_in_current_directory', '.txt')

Ваш
ответ:

('C:/Users/User/Documents', 'example', '.txt')
('', 'file_in_current_directory', '.txt')