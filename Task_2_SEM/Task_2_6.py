"""
Задание №6
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""
print('Программа Банкомат')
sum_ = 0
count_add = 0
count_out = 0

while True:
    if sum_ > 5000000:
        sum_ -= sum_ * 0.1
        print('С вас сняли налог на богатство')
    action = input('Введите тип действия:  ')
    if action == 'q':
        print('Выход изз банкомата')
        print(sum_)
        break
    elif action == 'a':
        sum_add = int(input('Ведите сумму'))
        if sum_add % 50 == 0:
            sum_ += sum_add
            count_add += 1
            if count_add % 3 == 0:
                sum_ *= 1.03
        else:
            print('Введена некорректная сумма не кратна 50')
    elif action == 'o':
        sum_out = int(input('Ведите сумму'))
        commission = sum_ * 0.015
        if commission <= 30:
            commission = 30
        elif commission > 600:
            commission = 600

        if sum_out + commission > sum_:
            print('Средств недостаточно')
        else:
            if sum_out % 50 == 0:
                sum_ -= sum_out + commission
                count_out += 1
                if count_out % 3 == 0:
                    sum_ *= 1.03
            else:
                print('Введена некоректная сумма')
    print(sum_)
