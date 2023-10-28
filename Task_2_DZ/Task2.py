'''
На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.

Напишите программу, которая должна возвращать сумму и произведение дробей.

Для проверки своего кода используйте модуль fractions.
'''

import fractions

frac1 = "1/2"
frac2 = "1/3"

num1, den1 = map(int, frac1.split('/'))
num2, den2 = map(int, frac2.split('/'))

denominators_sum = den1 * den2
nominators_sum = num1 * den2 + num2 * den1

nominators_mult = num1 * num2
denominators_mult = den1 * den2

print(f'Сумма дробей: {nominators_sum}/{denominators_sum}')
print(f'Произведение дробей: {nominators_mult}/{denominators_mult}')

print("Сумма дробей:", fractions.Fraction(frac1) + fractions.Fraction(frac2))
print("Произведение дробей:", fractions.Fraction(frac1) * fractions.Fraction(frac2))

# def add_fractions(frac1, frac2):
#     # Разделяем числитель и знаменатель первой дроби
#     num1, den1 = map(int, frac1.split('/'))
#     # Разделяем числитель и знаменатель второй дроби
#     num2, den2 = map(int, frac2.split('/'))
#
#     # Вычисляем общий знаменатель
#     common_denominator = den1 * den2
#
#     # Вычисляем сумму числителей
#     sum_num = num1 * den2 + num2 * den1
#
#     # Возвращаем сумму дробей
#     return f"{sum_num}/{common_denominator}"
#
#
# def multiply_fractions(frac1, frac2):
#     # Разделяем числитель и знаменатель первой дроби
#     num1, den1 = map(int, frac1.split('/'))
#     # Разделяем числитель и знаменатель второй дроби
#     num2, den2 = map(int, frac2.split('/'))
#
#     # Вычисляем произведение числителей
#     product_num = num1 * num2
#
#     # Вычисляем произведение знаменателей
#     product_den = den1 * den2
#
#     # Возвращаем произведение дробей
#     return f"{product_num}/{product_den}"
#
# # Пример использования
# frac1 = "2/3"
# frac2 = "3/4"
#
# sum_frac = add_fractions(frac1, frac2)
# product_frac = multiply_fractions(frac1, frac2)
#
# print("Сумма дробей:", sum_frac)
# print("Произведение дробей:", product_frac)
