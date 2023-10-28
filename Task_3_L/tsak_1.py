'''
Списки

list_1 = list()
list_2 = list((3.14, True, "Helloo world!"))
list_3 = []
list_4 = [3.14, True, "Helloo world!"]
'''

my_dist = {'one': 1, 'two': 2, 'three': 3, 'for': 4, 'ten': 10}
print(my_dist.items())

for key, value in my_dist.items():
    print(f'{key = } value before 100 - {100 - value}')

my_set = {1, 2, 3, 4, 5, 6, 7}
other_set = {1, 42, 4, 314}
print(my_set - other_set)

text_en = 'Hello world'
res = text_en.encode('utf-8')
print(res, type(res))

text_ru = 'Привет, мир'
res = text_ru.encode('utf-8')
print(res, type(res))

x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8')
y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')
print(f'{x = }\n{y = }')
