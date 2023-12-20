import logging

class NegativeValueError(Exception):
    def __init__(self, value, attribute):
        self.value = value
        self.attribute = attribute
        super().__init__(f"{attribute} должна быть положительной, а не {value}")


# Создаем логгер
logger = logging.getLogger('RectangleLogger')
logger.setLevel(logging.INFO)

# Создаем обработчик для записи логов в файл
file_handler = logging.FileHandler('rectangle_logs.log')
file_handler.setLevel(logging.INFO)

# Создаем форматирование логов
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)


class Rectangle:
    def __init__(self, width, height=None):
        self._width = None
        self._height = None
        self.width = width
        if height is not None:
            self.height = height
        else:
            self.height = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise NegativeValueError(value, "Ширина")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise NegativeValueError(value, "Высота")
        self._height = value

    def perimeter(self):
        perimeter_value = 2 * (self.width + self.height)

        # Добавляем логирование информации в файл
        logger.info(f"Вычислен периметр прямоугольника: {perimeter_value}")

        return perimeter_value