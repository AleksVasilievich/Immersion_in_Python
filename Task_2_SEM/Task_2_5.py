import cmath
from math import sqrt

"""
Задание №5
✔ Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня.
"""

"""
Комплексное число — это выражение вида a + bi, где a, b — действительные числа,
 а i — так называемая мнимая единица, символ, квадрат которого равен –1, 
 то есть i2 = –1. Число a называется действительной частью, 
 а число b — мнимой частью комплексного числа z = a + bi
"""

a = 10
b = - 50
c = 100

d = b ** 2 - (4 * a * c)

if d > 0:
    x1 = (-1 * b + sqrt(d) / (2 * a))
    x2 = (-1 * b - sqrt(d) / (2 * a))
    print(x1, x2)
elif d == 0:
    x1 = -b / (2 * a)
    print(x1)
else:
    real = round(-b / (2 * a), 4)
    imaginary = round(sqrt(abs(d)) / (2 * a), 4)
    x1 = complex(real, imaginary)
    x2 = complex(real, - imaginary)
    print(x1, x2)

# Вариант №2

a = 10
b = - 50
c = 100

d = b ** 2 - (4 * a * c)

if d > 0:
    x1 = (-1 * b + sqrt(d) / (2 * a))
    x2 = (-1 * b - sqrt(d) / (2 * a))
    print(x1, x2)
elif d == 0:
    x1 = -b / (2 * a)
    print(x1)
else:
    x1 = (- 1 * b + cmath.sqrt(complex(d))) / (2 * a)
    x2 = (- 1 * b - cmath.sqrt(complex(d))) / (2 * a)
    print(x1, x2)
