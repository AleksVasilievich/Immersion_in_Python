import csv

class NameValidator:
    def __set__(self, instance, value):
        if not value.istitle() or not value.isalpha():
            raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        instance.__dict__[self.name] = value

class Subject:
    def __set__(self, instance, value):
        if value not in instance.valid_subjects:
            raise ValueError(f"Предмет '{value}' не найден")
        instance.__dict__[self.name] = value

class MarkValidator:
    def __set__(self, instance, value):
        if not (isinstance(value, int) and 2 <= value <= 5):
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        instance.__dict__[self.name] = value

class TestResultValidator:
    def __set__(self, instance, value):
        if not (isinstance(value, int) and 0 <= value <= 100):
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        instance.__dict__[self.name] = value

class Student:
    name = NameValidator()
    subject = Subject()
    mark = MarkValidator()
    test_result = TestResultValidator()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.valid_subjects = self.load_valid_subjects(subjects_file)

    def load_valid_subjects(self, subjects_file):
        with open(subjects_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            return next(reader)

    def add_subject_info(self, subject, mark, test_result):
        self.subject = subject
        self.mark = mark
        self.test_result = test_result
        self.subjects[subject] = (mark, test_result)

    def average_mark(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет '{subject}' не найден")
        mark, test_result = self.subjects[subject]
        return (mark + test_result) / 2.0

    def overall_average_mark(self):
        total_mark = 0
        total_test_result = 0
        for subject, (mark, test_result) in self.subjects.items():
            total_mark += mark
            total_test_result += test_result
        return (total_mark + total_test_result) / (2 * len(self.subjects))

# Создаем экземпляр студента
student = Student("Иванов Иван Иванович", "subjects.csv")

# Добавляем информацию о предметах
student.add_subject_info("Математика", 4, 80)
student.add_subject_info("Физика", 5, 90)

# Выводим средний балл по тестам для каждого предмета
print(student.average_mark("Математика"))  # Выведет средний балл по Математике
print(student.average_mark("Физика"))  # Выведет средний балл по Физике

# Выводим общий средний балл
print(student.overall_average_mark())  # Выведет общий средний балл