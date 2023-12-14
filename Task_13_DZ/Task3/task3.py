class InvalidNameError(Exception):
    def __init__(self, name, message="Name should be a non-empty string."):
        self.name = name
        self.message = message
        super().__init__(f"Invalid name: {name}. {message}")

class InvalidAgeError(Exception):
    def __init__(self, age, message="Age should be a positive integer."):
        self.age = age
        self.message = message
        super().__init__(f"Invalid age: {age}. {message}")

class InvalidIdError(Exception):
    def __init__(self, ID, message="Id should be a 6-digit positive integer between 100000 and 999999."):
        self.ID = ID
        self.message = message
        super().__init__(f"Invalid id: {ID}. {message}")

class Person:
    def __init__(self, last_name, first_name, middle_name, age):
        if not last_name or not first_name or not middle_name:
            raise InvalidNameError('')
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(age)
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
            raise InvalidIdError(ID)
        self.ID = ID

    def get_level(self):
        return sum(int(digit) for digit in str(self.ID)) % 7



'''Принято системой !!!'''

employee = Employee("Bob", "Johnson", "Brown", 40, 12345)

# person = Person("Alice", "Smith", "Johnson", 25)
# print(person.get_age())
#
#
#
#
# print()

# person = Person("Alice", "Smith", "Johnson", -5)
#
#
#
#
# print()


# person = Person("", "John", "Doe", 30)
#
#
#
#
# print()