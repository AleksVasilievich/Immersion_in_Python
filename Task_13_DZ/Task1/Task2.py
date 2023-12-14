
class NegativeValueError(Exception):
    def __init__(self, value, attribute):
        self.value = value
        self.attribute = attribute
        super().__init__(f"{attribute} должна быть положительной, а не {value}")


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
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    def __sub__(self, other):
        return Rectangle(max(0, self.width - other.width), max(0, self.height - other.height))

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник шириной {self.width} и высотой {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


'''Решение принято системой !!!'''

r = Rectangle(-2)