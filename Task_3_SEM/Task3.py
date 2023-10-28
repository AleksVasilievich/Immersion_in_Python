"""
Задание №3
✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
"""

tuple_obj = (1, 2.1, True, None, 'string', 3, 4, 5, False, 'elem')
dct = {}
for el_1 in tuple_obj:
    obj_type = type(el_1)
    # print(obj_type)
    lst = []
    for el_2 in tuple_obj:
        if type(el_2) == obj_type:
            lst.append(el_2)
    dct[obj_type] = lst

print(dct)