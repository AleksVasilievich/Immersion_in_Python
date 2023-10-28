"""
Задание №6
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""

lst = [1, 3, -5, 7, 5, 8, 4, -9, 2]

ind1 = 2
ind2 = 4


def func(lst, ind1, ind2):
    if ind1 >= ind2:
        # ind1, ind2 = ind2, ind1
        print("No element")
    elif ind1 < 0:
        return sum(lst[:ind2])
    elif ind2 > len(lst):
        return sum(lst[ind1 + 1:])
    else:
        return sum(lst[ind1 + 1:ind2])


print(func(lst, ind1, ind2))


def func1(lst, inx1, inx2):
    if inx1 >= inx2:
        print("No elements")
        return
    elif inx1 < 0 and inx2 > len(lst):
        return sum(lst)
    elif inx1 < 0:
        return sum(lst[:inx2])
    elif inx2 > len(lst):
        return sum(lst[inx1 + 1:])
    else:
        return sum(lst[inx1 + 1:inx2])

print(func1(lst, ind1, ind2))
