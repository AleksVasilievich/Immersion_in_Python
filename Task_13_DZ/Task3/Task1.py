'''
В организации есть два типа людей: сотрудники и обычные люди.
Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая)
Возраст (целое положительное число)
Сотрудники имеют также уникальный идентификационный номер (ID),
который должен быть шестизначным положительным целым числом.
Ваша задача:
Создать класс Person, который будет иметь атрибуты и методы для управления
данными о людях (Фамилия, Имя, Отчество, Возраст).
Класс должен проверять валидность входных данных и
генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.
Создать класс Employee, который будет наследовать класс Person и
добавлять уникальный идентификационный номер (ID).
Класс Employee также должен проверять валидность ID и
генерировать исключение InvalidIdError, если ID неверный.
Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
Добавить метод get_level в класс Employee,
который будет возвращать уровень сотрудника
на основе суммы цифр в его ID (по остатку от деления на 7).
Создать несколько объектов класса Person и Employee с разными данными и проверить,
что исключения работают корректно при передаче неверных данных.
'''

class InvalidNameError(Exception):
    pass

class InvalidAgeError(Exception):
    pass


class InvalidIdError(Exception):
    pass

class Person:
    def __init__(self, last_name, first_name, middle_name, age):
        if not last_name or not first_name or not middle_name:
            raise InvalidNameError("Invalid name")
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError("Invalid age")
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

class Employee(Person):
    def __init__(self, last_name, first_name, middle_name, age, ID):
        super().__init__(last_name, first_name, middle_name, age)
        if not isinstance(ID, int) or ID < 100000 or ID > 999999:
            raise InvalidIdError("Invalid ID")
        self.ID = ID

    def get_level(self):
        return sum(int(digit) for digit in str(self.ID)) % 7

# try:
#     person1 = Person("Иванов", "Иван", "Петрович", 25)
#     person2 = Person("Петров", "Петр", "Иванович", -5)  # вызовет исключение InvalidAgeError
# except InvalidAgeError as e:
#     print(e)
#
# try:
#     employee1 = Employee("Сидоров", "Игорь", "Владимирович", 30, 12345)  # вызовет исключение InvalidIdError
#     employee2 = Employee("Смирнова", "Ольга", "Алексеевна", 40, 987654)
# except InvalidIdError as e:
#     print(e)

# person = Person("Alice", "Smith", "Johnson", 25)
# print(person.get_age())

person = Person("Alice", "Smith", "Johnson", -5)




print()