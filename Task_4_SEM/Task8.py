"""
Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""

names = ['Alex', 'Nick', 'Michael']
count = 1
tapes = 1500
txt = 'Test'
rows = 'first'
s = -15
sym_calls = True

my_dict = globals().copy()
print(my_dict)

my_new_dict = {}
for k in my_dict.keys():
    if not k.startswith('__'):
        my_new_dict[k] = my_dict[k]

for k in my_new_dict.copy().keys():
    if k.endswith('s') and len(k) > 1:
        my_new_dict[k[:-1]] = my_new_dict[k]
        my_new_dict[k] = None

print(my_new_dict)

def rename():
    print()