"""
Напишите функцию для транспонирования матрицы transposed_matrix,
принимает в аргументы matrix, и возвращает транспонированную матрицу.
Пример использования На входе:

matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
transposed_matrix = transpose(matrix)         На выходе:    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
"""

def transpose(matrix):
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

transposed_matrix = transpose(matrix)
print(matrix)
print(transposed_matrix)




# trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         trans_matrix[j][i] = matrix[i][j]
# print(trans_matrix)




# print(transposed_matrix)