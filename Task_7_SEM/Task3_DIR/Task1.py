from random import randint, choice
from math import floor

'''
Задание №3
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла, возвращайтесь  в его начало.
'''


def names_and_nums(file_name):
    with (
        open('../Task2_DIR/task_2.txt', 'r', encoding='utf-8') as names,
        open('../Task1_DIR/file_txt.txt', 'r', encoding='utf-8') as nums,
        open(file_name, 'w', encoding='utf-8') as res
    ):
        names_list = list(names)
        nums_list = list(nums)
        max_len = max(len(names_list), len(nums_list))
        # names_final, nums_final = [], []
        for i in range(max_len):
            '''
            Если длина списков разная то индекс [i % len(names_list)] или [i % len(nums_list)] позволяет 
            -ходить покругу- то есть за последним индексом будет идти нулевой и так далее...
            '''
            name = names_list[i % len(names_list)].strip() # strip() позволяет не переходить на новую строку
            num = int(nums_list[i % len(nums_list)].split(' | ')[0]) * float(
                nums_list[i % len(nums_list)].split(' | ')[1])
            if num >= 0:
                print(f'{name.upper()} - {floor(num)}', file=res)
            else:
                print(f'{name.lower()} - {abs(num)}', file=res)




if __name__ == '__main__':
    names_and_nums('task_3.txt')
