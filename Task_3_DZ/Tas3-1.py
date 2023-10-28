def pack_backpack(items, max_weight, current_weight=0, current_items={}):
    if current_weight > max_weight:
        return []

    result = [current_items]

    for item, weight in items.items():
        new_weight = current_weight + weight
        new_items = dict(current_items)
        new_items[item] = weight
        result += pack_backpack(items, max_weight, new_weight, new_items)

    return result


items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

result = pack_backpack(items, max_weight)
print(result)