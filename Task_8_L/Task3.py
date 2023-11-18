'''
● Преобразование Python в JSON
Что делать, если мы хотим превратить Словарь Python в JSON объект? Для этого
используем функции сериализации dump и dumps. Смысл окончания s у dumps
такой же как и у loads.

'''

import json

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование",
                "путешествия"],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}
print(f'{type(my_dict) = }\n{my_dict = }')
with open('new_user.json', 'w') as f:
    json.dump(my_dict, f)

"""
Если же мы хотим отказаться от символов экранирования в JSON файле, следует
установить дополнительный параметр ensure_ascii в значение ложь.
"""

# with open('new_user.json', 'w', encoding='utf-8') as f:
#     json.dump(my_dict, f, ensure_ascii=False)
