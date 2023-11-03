'''
Вы работаете над разработкой программы для проверки корректности даты,
введенной пользователем. На вход будет подаваться дата в формате "день.месяц.год".
Ваша задача - создать программу, которая проверяет,
является ли введенная дата корректной или нет.

Ваша программа должна предоставить ответ "True" (дата корректна)
или "False" (дата некорректна) в зависимости от результата проверки.
Пример использования
На входе:    date_to_prove = 15.4.2023
На выходе:   True

На входе:    date_to_prove = 31.6.2022
На выходе:   False
'''


data_to_prove = '29.2.2020'

data = [int(i) for i in data_to_prove.split('.')]
flag = True
if (1 > data[0] or data[0] > 31) or (1 > data[1] or data[1] > 12) or (1 > data[2] or data[2] > 9999):
    flag = False
if data[0] == 31 and data[1] in [int(i) for i in '2,4,6,9,11'.split(',')] :
    flag = False
if (data[0] == 31 or data[0] == 30) and data[1] == 2:
    flag = False
if ''.join(str(data[2])[2:]) == '00' and data[2] % 400 == 0 and data[0] == 28 and data[1] == 2:
    flag = False
if ''.join(str(data[2])[2:]) != '00' and data[2] % 4 == 0 and data[0] == 28 and data[1] == 2:
    flag = False
if ''.join(str(data[2])[2:]) != '00' and data[2] % 4 != 0 and data[0] == 29 and data[1] == 2:
    flag = False
if ''.join(str(data[2])[2:]) == '00' and data[2] % 400 != 0 and data[0] == 29 and data[1] == 2:
    flag = False

print(flag)

