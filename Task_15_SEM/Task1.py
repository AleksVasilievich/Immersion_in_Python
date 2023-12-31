"""
Задание №1
📌 Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
📌 Например отлавливаем ошибку деления на ноль.
"""

import logging

logging.basicConfig(filename='C:\\Users\Aleksandr\PycharmProjects\python_GB_2\Logs\log_1.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке {lineno} '
                           'функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.ERROR)
logger = logging.getLogger(__name__)


def division(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        logger.error(
            f'Ошибка деления на ноль! Число {a} нельзя поделить на число {b}')
        return float('inf')
    return res


if __name__ == '__main__':
    print(f'{division(15, 0)}')
