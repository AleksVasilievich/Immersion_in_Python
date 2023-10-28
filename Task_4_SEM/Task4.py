from timeit import timeit

"""
Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
"""

lst = [2, 4, 7, 9, 1, 3]

def bubble_sort(nums):  # Сортировка пузырьком
    n = 1
    while n < len(nums):
        for i in range(len(nums) - n):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i +1] = nums[i + 1], nums[i]
        n += 1
    return nums

# print(bubble_sort(lst))

'''
Замеры на скорость выполнения
'''

print(timeit('bubble_sort(lst)', globals=globals(), number=1000000))