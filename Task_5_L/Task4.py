# def factorial(n):
#     namber = 1
#     result = []
#     for i in range(1, n + 1):
#         namber *= i
#         result.append(namber)
#     return result
#
# for i, num in enumerate(factorial(10), start=1):
#     print(f'{i}! = {num}')
#
# print()
#
# def factorial(n):
#     namber = 1
#     for i in range(1, n + 1):
#         namber *= i
#         yield namber
#
# for i, num in enumerate(factorial(10), start=1):
#     print(f'{i}! = {num}')
# print()
#

def factorial(n):
    namber = 1
    for i in range(1, n + 1):
        namber *= i
        yield namber

my_iter = iter(factorial(4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
