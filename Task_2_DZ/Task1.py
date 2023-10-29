'''
Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''

# def decimal_to_hex(num):
#     hex_chars = "0123456789ABCDEF"
#
#     if num == 0:
#         return "0"
#
#     hex_string = ""
#     while num > 0:
#         remainder = num % 16
#         hex_string = hex_chars[remainder] + hex_string
#         num = num // 16
#
#     return hex_string
#
# # Пример использования
# num = int(input("Введите целое число: "))
# hex_str = decimal_to_hex(num)
# print("Шестнадцатеричное представление числа:", hex_str)
#

num = 255
num1 = num

hex_chars = "0123456789ABCDEF"

if num == 0:
    print('')

hex_string = ""
while num > 0:
    remainder = num % 16
    hex_string = hex_chars[remainder] + hex_string
    num = num // 16

print('Шестнадцатеричное представление числа:', hex_string)
print('Проверка результата:', hex(num1))