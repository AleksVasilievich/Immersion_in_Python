'''
4. Декоратор @property
На прошлой лекции мы работали с классом треугольник и пометили его свойства
защищёнными, добавив символ подчёркивания в начале имени. Но что если доступ
к свойству нужен. Хотя бы на чтение. Для этого отлично подойдёт функция
декоратор property(). Рассмотрим на более простом и коротком примере.
'''

class User:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name


user = User('Стивен')
print(f'{user.name = }')
#user.name = 'Славик' # AttributeError: can't set attribute 'name'
