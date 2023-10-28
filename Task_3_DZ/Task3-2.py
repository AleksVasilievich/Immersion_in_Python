def find_backpack(items, max_weight):
    backpack = {}  # словарь с вещами в рюкзаке
    result = []  # список всех возможных вариантов backpack

    def backtrack(items, max_weight, current_weight, current_items):
        if current_weight > max_weight:
            return

        if current_weight <= max_weight:
            result.append(current_items.copy())

        for item in items:
            if item not in current_items:
                current_items[item] = items[item]
                current_weight += items[item]

                backtrack(items, max_weight, current_weight, current_items)

                current_items.pop(item)
                current_weight -= items[item]

    backtrack(items, max_weight, 0, backpack)

    return result

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

result = find_backpack(items, max_weight)
print(result)