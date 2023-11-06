
def is_attacking(q1, q2):
    # Проверка, бьют ли ферзи друг друга
    x1, y1 = q1
    x2, y2 = q2
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

def check_queens(queens):
    # Проверка всех возможных пар ферзей
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False
    return True

# Функция для получения координат ферзей от пользователя
def get_queen_coordinates():
    queens = []
    for i in range(8):
        x, y = map(int, input("Введите координаты ферзя (через пробел): ").split())
        queens.append((x, y))
    return queens

# Получаем координаты ферзей от пользователя
queens = get_queen_coordinates()

# Проверяем, бьют ли ферзи друг друга
result = check_queens(queens)

# Выводим результат
if result:
    print("Ферзи не бьют друг друга")
else:
    print("Ферзи бьют друг друга")