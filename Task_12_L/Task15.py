
'''
5. Дескрипторы
Дескриптор - это атрибут объекта со “связанным поведением”, то есть такой
атрибут, при доступе к которому его поведение переопределяется методом
протокола дескриптора. Эти методы __get__, __set__ и __delete__. Если хотя бы
один из этих методов определен в объекте , то можно сказать что этот метод
дескриптор.
Звучит немного сложно. Так и есть. Дескрипторы не нужны для простых классов. Их
польза проявляется при метапрограммировании, создании фреймворков.
Посмотрите на то как в Django создаются модели для работы с базой данных.
Пример взят из официальной документации
'''

from django.db import models
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

'''Как и почему работает код, где на уровне класса в обход инициализации создаются
два свойства как экземпляры другого класса? Под капотом работают дескрипторы.
Напишем класс, который хранит имя ученика, его возраст, номер класса (от 1 до 11)
и номер кабинета, в котором сидит класс.
'''

class Student:
    def __init__(self, name, age, grade, office):
        self.name = name
        self.age = age
        self.grade = grade
        self.office = office
    def __repr__(self):
        return f'Student(name={self.name}, age={self.age},grade={self.grade}, office={self.office})'
std1 = Student('Шурик', 7, 1, 12)
print(std1)
