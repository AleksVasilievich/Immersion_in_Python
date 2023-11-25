'''
Задание
Перед вами несколько строк кода. Какие ошибки и недочёты есть в коде. У вас 3
минуты.
'''


class User:
    def __init__(self, name, phone, password):
        self.__name__ = name  # Использование магических методов не правильно !
        self._phone = phone
        self.__password = password


u1 = User('One', '123-45-67', 'qwerty')
print(f'{u1.__name__ = }, {u1._phone = }, {u1._User__password = }')
# Использование защищённой и приватной переменной вне класса не правильно !
