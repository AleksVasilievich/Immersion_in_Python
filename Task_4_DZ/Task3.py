"""
У вас есть банковская карта с начальным балансом равным 0 у.е.
Вы хотите управлять этой картой, выполняя следующие операции, для выполнения которых
необходимо написать следующие функции: check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
deposit(amount): Пополнение счёта.     withdraw(amount): Снятие денег.
exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.
Пополнение счета:
Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму.
Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.
Снятие средств:
Функция withdraw(amount) позволяет клиенту снимать средства со счета.
Сумма снятия также должна быть кратной MULTIPLICITY. При снятии средств начисляется комиссия
в процентах от снимаемой суммы, которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.
Завершение работы: Функция exit() завершает работу с банковским счетом. Перед завершением, если на счету больше
RICHNESS_SUM, начисляется налог на богатство в размере RICHNESS_PERCENT процентов.
Проверка кратности суммы:
Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY.
Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.

На входе:
deposit(10000)
withdraw(4000)
exit()

print(operations)

На выходе:
['Пополнение карты на 10000 у.е. Итого 10000 у.е.', 'Снятие с карты 4000 у.е. Процент за снятие 60 у.е.. Итого 5940 у.е.']

"""
from decimal import Decimal
from random import *

MULTIPLICITY = 5
MIN_REMOVAL = 2
MAX_REMOVAL = 7
RICHNESS_SUM = 100000
RICHNESS_PERCENT = 10
balance = 0
balance = Decimal(balance)
deposit_list = []

def check_multiplicity(amount):
    if amount % MULTIPLICITY == 0:
        return True
    else:
        return False

def deposit(amount):
    global balance
    if check_multiplicity(amount):
        balance += amount
        deposit_list.append(f'Пополнение карты на {amount} у.е.')
    else:
        print(f'Пополнение карты возможно только суммой кратной {MULTIPLICITY}')




def withdraw(amount):
    global balance
    if check_multiplicity(amount):
        i = random() * randrange(MIN_REMOVAL, MAX_REMOVAL)
        balance -= amount
        balance -= amount % i
        deposit_list.append(f'Снятие с карты на {amount} у.е.')
    else:
        print(f'Снятие со карты возможно только суммой кратной {MULTIPLICITY}')




def exit():
    global deposit_list
    deposit_list.append(f'Итого {balance} у.е.')
    print(deposit_list)


deposit(1000)
withdraw(200)
exit()

# print(operations)
