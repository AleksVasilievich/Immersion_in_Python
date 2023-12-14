from typing import Union

class InvalidTextError(Exception):
    pass

class InvalidNumberError(Exception):
    pass

class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей
    - archive_number (list): список архивированных числовых записей
    """

    def __init__(self, text: str, number: Union[int, float]):
        self.archive_text = []
        self.archive_number = []
        self.add_text(text)
        self.add_number(number)

    def add_text(self, text: str):
        if not isinstance(text, str) or text == "":
            raise InvalidTextError(f"Invalid text: {text}. Text should be a non-empty string.")
        self.archive_text.append(text)

    def add_number(self, number: Union[int, float]):
        if not (isinstance(number, int) and number > 0) and not isinstance(number, float):
            raise InvalidNumberError(f"Invalid number: {number}. Number should be a positive integer or float.")
        self.archive_number.append(number)

    def __str__(self):
        return f"Text is {self.text} and number is {self.number}. Also [] and []"

# # Пример использования
# try:
#     invalid_archive_instance = Archive("Sample text", -5)
#     print(invalid_archive_instance)
# except (InvalidTextError, InvalidNumberError) as e:
#     print(f"Ошибка: {e}")

archive_instance = Archive("Sample text", 42.5)
print(archive_instance)