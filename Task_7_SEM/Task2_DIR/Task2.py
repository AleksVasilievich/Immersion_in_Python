"""
✔ Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
среди которых обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""
import random


def generation_name():
    vowels ='aeiouy'
    consonants = 'bcdfghjklmnpqrstvwxz'
    name_len = random.randint(4, 7)
    name = [random.choice(vowels + consonants).upper()]
    for i in range(name_len -1):
        name.append(random.choice(consonants))
    for i in range(name_len -1 // 2):
        name[random.choice(range(1, name_len -1))] = random.choice(vowels)
    return ''.join(name)

def save_names(count, file_name):
    with open(file_name, 'a', encoding='utf=8') as file:
        for _ in range(count):
            print(generation_name(), file=file) # печатаем в файл


if __name__ == '__main__':
    save_names(5, "task_2.txt")