#
# data = [2, 4, 6, 8]
# list_iter = iter(data)
# print(list_iter)
#
#
# data = [2, 4, 6, 8]
# list_iter = iter(data)
# print(*list_iter)  # Функция iter() работает один раз
# print(*list_iter)
#
# data = [2, 4, 6, 8]

import functools

f = open('C:\\Users\Aleksandr\PycharmProjects\python_GB_2\mydata.bin', 'rb')
for block in iter(functools.partial(f.read, 16), b''):
    print(block)
f.close()