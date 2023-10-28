"""
Задание №1
✔ Вручную создайте список с целыми числами, которые
повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.
✔ *Подготовьте два решения, короткое и длинное, которое
не использует другие коллекции помимо списков
"""

# №1

data = [1, 3, 5, 1, 3, 7, 9]
print(list(set(data)))

# №2

res = []
for item in data:
    if item not in res:
        res.append(item)

print(res)