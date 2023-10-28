"""
Задание №3
✔ Напишите программу, которая получает целое число и возвращает
его двоичное, восьмеричное строковое представление.
✔ Функции bin и oct используйте для проверки своего
результата, а не для решения.
Дополнительно:
✔ Попробуйте избежать дублирования кода
в преобразованиях к разным системам счисления
✔ Избегайте магических чисел
✔ Добавьте аннотацию типов где это возможно
"""
# https://calcus.ru/perevod-sistem-schisleniya/iz-desyatichnoy-v-vosmerichnuyu
# перевод числа из десятичного в двоичное

num = 123
print(bin(num))
base = 2
res = ""

while num > 0:
    res = str(num % base) + res
    num //= base
print(res)

num = 123
print(oct(num))

base: int = 8
res: str = ""

while num > 0:
    res = str(num % base) + res
    num //= base
print(res)

