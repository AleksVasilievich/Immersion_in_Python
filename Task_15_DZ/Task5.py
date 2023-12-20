import argparse
import logging

logging.basicConfig(filename='C:\\Users\Aleksandr\PycharmProjects\python_GB_2\Logs\log_1.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке {lineno} '
                           'функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.NOTSET)
logger = logging.getLogger(__name__)


def division(a, b):
    try:
        res = a / b
        logger.info(f'{a} / {b} = {res}')
    except ZeroDivisionError:
        logger.error(
            f'Ошибка деления на ноль! Число {a} нельзя поделить на число {b}')
        return float('inf')
    return res


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Принимаем строку')
    parser.add_argument('-a', metavar='a', type=float, help='Справка')
    parser.add_argument('-b', metavar='b', type=float, help='Справка')
    args = parser.parse_args()

    print(division(args.a, args.b))


