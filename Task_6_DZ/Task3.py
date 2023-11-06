'''
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей
на шахматной доске, в которой ни один ферзь не бьет другого. Другими словами,
ферзи размещены таким образом, что они не находятся на одной вертикали,
горизонтали или диагонали.
Список из 4х комбинаций координат сохраните в board_list.
 Дополнительно печатать его не надо.

Пример использования На входе:    print(generate_boards())
На выходе:
[[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)],
[(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)],
[(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)],
[(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]]
'''

import random

'''
Принято системой
'''


def is_attacking(q1, q2):
    x1, y1 = q1
    x2, y2 = q2
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)


def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False
    return True


def generate_boards():
    board_list = []
    while len(board_list) < 4:
        queens = []
        for i in range(8):
            queen = (i + 1, random.randint(1, 8))
            queens.append(queen)

        if check_queens(queens):
            board_list.append(queens)

    return board_list



print(generate_boards())





