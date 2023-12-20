import argparse
import logging

logging.basicConfig(filename='C:\\Users\Aleksandr\PycharmProjects\python_GB_2\Logs\log_5.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке {lineno} '
                           'функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        res = 2 * (self._width + self._height)
        logger.info(f'width {self._width} height {self.height} perimeter {res}')
        return res

    def area(self):
        res = self._width * self._height
        logger.info(f'width {self._width} height {self.height} area {res}')
        return res

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter:
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Принимаем строку')
    parser.add_argument('-wi', metavar='wi', type=int, help='Справка')
    parser.add_argument('-he', metavar='he', type=int, help='Справка')
    args = parser.parse_args()

    rect = Rectangle(args.wi, args.he)
    print(rect.perimeter())
    print(rect.area())

    # try:
    #     width = args.w
    #     height = args.h if args.h is not None else args.w
    #     rectangle = Rectangle(width, height)
    #
    #     perimeter = rectangle.width * 2 + rectangle.height * 2
    #     logger.info("Пользователь ввел параметры w=%s и h=%s", width, height)
    #     logger.info("Периметр прямоугольника: %s", perimeter)
    #
    # except NegativeValueError as e:
    #     logger.error(str(e))
    #
    # except argparse.ArgumentError as e:
    #     logger.error("Ошибка ввода параметров 1: %s", e)
    #
    # except Exception as e:
    #     logger.error("Произошла ошибка 2: %s", e)

# ren = Rectangle(5, 2).area()
# ren1 = Rectangle(3, 7).perimeter()
# print(ren)
# print(ren1)
