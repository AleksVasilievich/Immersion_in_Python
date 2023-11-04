"""
Задание №4
✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите
числа, сумма цифр которых равна 8.
✔ Решение в одну строку.
"""

even_get = (num for num in range(0, 100, 2) if sum([int(digit) for digit in str(num)]) != 8)

# print(*even_get) # так

# print(list(even_get))  # или так

for i in even_get:
    print(i)             #  или так
