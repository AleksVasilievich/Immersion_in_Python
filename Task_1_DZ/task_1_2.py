# Напишите код, который анализирует число num и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


num = 158

def prime_number(num):
    if num > 1 and num < 100000:
        for i in range(2, num):
            if num % i == 0:
                return print(num, "является составным числом")

        print(num, "является простым числом")
    else:
        print("Число должно быть больше 1 и меньше 100000")


if __name__ == '__main__':
    prime_number(num)