from itertools import combinations


items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

result = []

keys = list(items.keys())
values = list(items.values())

for r in range(1, len(items) + 1):
    for indices in combinations(range(len(items)), r):
        total_weight = sum([values[i] for i in indices])
        if total_weight <= max_weight:
            combination = {keys[i]: values[i] for i in indices}
            result.append(combination)

print(result)