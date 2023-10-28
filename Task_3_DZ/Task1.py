"""
На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.
Пример
На входе:

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

На выходе:

{'ключи': 0.3, 'кошелек': 0.2, 'зажигалка': 0.1}
"""

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

backpack = {}

for item, weight in items.items():
    if weight <= max_weight:
        backpack[item] = weight  # программа выдаёт это решение
        max_weight -= weight

print(backpack)




# def backpack(items, max_weight):
#     sum = 0
#     backpack = {}
#
#     for key, value in items.items():      # Моё решение !
#         sum += value
#         if sum <= max_weight:
#             backpack[key] = value
#         else:
#             sum = sum - value
#     print(backpack)
#
# backpack(items,max_weight)


# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0
#
#
#
#         print(f'{key:}\t{value}')


# backpack = {key: value for key, value in items.items() if value < max_weight }
# print(backpack)