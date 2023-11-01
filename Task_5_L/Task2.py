
data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)


data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)  # Функция iter() работает один раз
print(*list_iter)