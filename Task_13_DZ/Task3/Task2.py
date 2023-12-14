class InvalidNameError(Exception):
    pass

class InvalidAgeError(Exception):
    def __init__(self, age, message="Age should be a positive integer"):
        self.age = age
        self.message = message
        super().__init__(f"Invalid age: {age}. {message}")

class Person:
    def __init__(self, last_name, first_name, middle_name, age):
        if not last_name or not first_name or not middle_name:
            raise InvalidNameError("Invalid name")
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError()
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

person = Person("Alice", "Smith", "Johnson", -5)