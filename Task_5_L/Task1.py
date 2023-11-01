
#
# a = 48
# b = 75
# a, b = b, a
# print(a, b)
#
#
# a, b, c = input()
# print(f'{a=} {b=} {c=}')
#
#
# a, b, c = ('один', 'два', 'три')
# print(f'{a=} {b=} {c=}')
#
#
# data = ['один', 'два', 'три' , 'четыре', 'пять', 'шесть', 'семь', ]
# a, b, c, *d = data
# print(f'{a=} {b=} {c=} {d=}')
# a, b, *c, d = data
# print(f'{a=} {b=} {c=} {d=}')
# a, *b, c, d = data
# print(f'{a=} {b=} {c=} {d=}')
# *a, b, c, d = data
# print(f'{a=} {b=} {c=} {d=}')
#
#
# link = 'https://pythonist.ru/top-8-bibliotek-python-dlya-mashinnogo-obucheniya-i-iskusstvennogo-intellekta/fgh'
# prefix, *_, suffix = link.split('/')    # Подчёркивание после звёздочки это некая мусорная корзина,
#                                         # Значения упаквываются , но больше не используются
# print(suffix)
# print(prefix)
#
#
# data = [2, 4, 6, 8, 10, ]
# for item in data:
#     print(item, end='\t')
# print()
#
# print(*data, sep='\t')  # Аналогичный вывод без цикла


a = b = c = 0   #Хорошо
a += 42
print(f'{a=} {b=} {c=}')

a = b = c = {1, 2, 3}  # Плохо
a.add(42)
print(f'{a=} {b=} {c=}')

a, b, c = 1, 2, 3
print(f'{a=} {b=} {c=}')

t = 1, 2, 3
print(f'{t=}, {type(t)}')

a = b = c = 42
# if a == b and b == c:  # Аналогично
if a == b == c:
    print('Полное совпадение')

if a > b > c:
    print('b Больше а и меньше c')
