'''
Сколько комбинаций можно составить из 4 предметов
В различных задачах встречается необходимость рассчитать количество возможных комбинаций из некоторого количества объектов. Для этого используется формула:

C(n, k) = n! / (k! * (n-k)!)

где n — общее количество объектов, k — количество объектов в комбинации.

Для примера находим количество комбинаций из 4 предметов.
'''



from itertools import combinations

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}

result = []

# Получаем ключи и значения из словаря
keys = list(items.keys())
values = list(items.values())

# Генерируем все комбинации от 1 до размера словаря
for r in range(1, len(items) + 1):
    # Генерируем комбинации индексов с помощью функции combinations
    for indices in combinations(range(len(items)), r):
        # Создаем словарь с текущей комбинацией
        combination = {keys[i]: values[i] for i in indices}
        result.append(combination)

print(result)