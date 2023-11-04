"""
Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""

num = 20
def gen_primes(n):
    primes = []
    current_number = 2
    while len(primes) < n:
        is_prime = all(current_number % prime != 0 for prime in primes)
        if is_prime:
            primes.append(current_number)
            yield current_number
        current_number += 1

nums = gen_primes(num)
for i in nums:
    print(i)