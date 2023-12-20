import time
from datetime import datetime
class MyStr(str):
    """
    Класс для создания строки с информацией об авторе и времени создания.

    Атрибуты:
    value (str): строковое значение.
    author (str): имя автора.

    Dunder методы:
    __new__(cls, value, author): создает новый объект класса.
    __str__(): возвращает строковое представление объекта класса.
    __repr__(): возвращает строковое представление объекта класса для отладки.

    """

import argparse
import logging


logging.basicConfig(filename='C:\\Users\Aleksandr\PycharmProjects\python_GB_2\Logs\log_1.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке {lineno} '
                           'функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

class MyStr(str):

    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance

    def __str__(self):
        formatted_time = datetime.fromtimestamp(self.time).strftime('%Y-%m-%d %H:%M')
        logger.info(f'Инфо')
        return f"{super().__str__()} (Автор: {self.author}, Время создания: {formatted_time})"

    def __repr__(self):
        return f"MyStr('{super().__str__()}', '{self.author}')"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Принимаем строку')
    parser.add_argument('-a', metavar='a', type=float, help='Справка')
    parser.add_argument('-b', metavar='b', type=float, help='Справка')
    args = parser.parse_args()

    print()