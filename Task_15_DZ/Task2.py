import argparse
import logging

logging.basicConfig(filename='rectangle_logs.log',
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
