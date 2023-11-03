

data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))

print()

data = {"один": 1, "два": 2, "три": 3}
x = iter(data.items())
print(x)
print(x)
y = next(x)
print(y)
print(y)
z = next(iter(y))
print(z)
print(z)

print()

# генератор

a = range(0, 10, 2)
print(f'{a=}, {type(a)=}, {a.__sizeof__()=}, {len(a)}')

b = range(-10_000_000, 1_000_000)
print(f'{b=}, {type(b)=}, {b.__sizeof__()=}, {len(b)}')

# генераторные выражения

me_gen = (chr(i) for i in range(97, 123))
print(me_gen)
for char in me_gen:
    print(char)


x = [1, 1, 3, 4, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')

res = [i + j for i in x if i % 2 != 0 for j in y if j != 1]
print(f'{len(res)=}\n{res}')
print()

mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
res = list(mult)
print(f'{len(res)=}\n{res}')
print()

res = {i + j for i in x if i % 2 != 0 for j in y if j != 1}
print(f'{len(res)=}\n{res}')
print()

mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
for item in mult:
    print(f'{item = }')

print()


my_setcomp = {chr(i) for i in range(97, 123)}
print(my_setcomp)
for char in  my_setcomp:
    print(char)
print()

my_distcomp = {i: chr(i) for i in range(97, 123)}
print(my_distcomp)
for namber, char in  my_distcomp.items():
    print(f'dist[{namber}] = {char}')
print()


# задача

data = {2, 4, 4, 6, 8, 10, 12}
res1 = {None: item for  item in data if item > 4}
res2 = (item for  item in data if item > 4)
res3 = [[item] for  item in data if item > 4]
print(res1, res2, res3)
