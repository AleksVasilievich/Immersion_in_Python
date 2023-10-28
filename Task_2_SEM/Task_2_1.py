"""
Задание №1
Создайте несколько переменных разных типов.
Проверте к какому типу относятся созданные переменные.
"""

data = [1, True,'text', 1.2, None, b'12']

for item in data:
    print(type(item))

for i in range(1, len(data)):
    print(type(data[i]))

for item in data[1:]:
    print(type(item))
    