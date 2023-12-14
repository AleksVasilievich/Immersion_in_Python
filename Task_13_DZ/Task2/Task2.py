from typing import Union

class InvalidTextError(Exception):
    pass

class InvalidNumberError(Exception):
    pass

class Archive:

    def __init__(self):
        self.archive_text = []
        self.archive_number = []
        self.text = ""
        self.number = 0

    def add_text(self, text: str):
        if not isinstance(text, str) or text == "":
            raise InvalidTextError(f"Invalid text: {text}. Text should be a non-empty string.")
        self.archive_text.append(text)

    def add_number(self, number: Union[int, float]):
        if not (isinstance(number, int) and number > 0) and not isinstance(number, float):
            raise InvalidNumberError(f"Invalid number: {number}. Number should be a positive integer or float.")
        self.archive_number.append(number)

# # Пример использования
# archive = Archive()
#
# try:
#     archive.add_text(123)  # вызовет InvalidTextError
# except InvalidTextError as e:
#     print(f"Ошибка: {e}")
#
# try:
#     archive.add_number(-12)  # вызовет InvalidNumberError
# except InvalidNumberError as e:
#     print(f"Ошибка: {e}")

invalid_archive_instance = Archive("Sample text", -5)
print(invalid_archive_instance)

archive_instance = Archive("Sample text", 42.5)
print(archive_instance)