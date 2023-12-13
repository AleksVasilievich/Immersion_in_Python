import csv

class Student:
    def __init__(self, name, subjects_file):
        self.__name = name
        self.__subjects = {}
        self.load_subjects(subjects_file)

    def __setattr__(self, name, value):
        if name == "name" and not value.istitle():
            raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        object.__setattr__(self, name, value)

    def __getattr__(self, name):
        if name in self.__subjects:
            raise ValueError(f"Предмет '{name}' не найден")
        object.__dict__[self.name] = name

    def add_grade(self, subject, grade):
        if grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self.__subjects[subject] = {"grades": [grade], "test_scores": []}

    def add_test_score(self, subject, test_score):
        if test_score < 0 or test_score > 100:
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        self.__subjects[subject]["test_scores"].append(test_score)

    def get_average_grade(self):
        total_grades = 0
        num_grades = 0
        for subject in self.__subjects.values():
            total_grades += sum(subject["grades"])
            num_grades += len(subject["grades"])
        return total_grades / num_grades if num_grades > 0 else 0

    def get_average_test_score(self, subject):
        if subject in self.__subjects and self.__subjects[subject]["test_scores"]:
            return sum(self.__subjects[subject]["test_scores"]) / len(self.__subjects[subject]["test_scores"])
        else:
            return 0

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                subject = row[0]
                self.__subjects[subject] = {"grades": [], "test_scores": []}

    def __str__(self):
        return f"Студент: {self.__name}\nПредметы: {', '.join(self.__subjects.keys())}"

 '''Принят системой !'''

# Пример использования
student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)