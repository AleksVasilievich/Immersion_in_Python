import decimal

MULTIPLICITY = 50  # множитель, кратность суммы
MIN_REMOVAL = 0.02  # минимальная комиссия за снятие в долях от снимаемой суммы
MAX_REMOVAL = 0.05  # максимальная комиссия за снятие в долях от снимаемой суммы
RICHNESS_SUM = 10000  # сумма, после которой начисляется налог на богатство
RICHNESS_PERCENT = 0.1  # процент налога на богатство

balance = decimal.Decimal(0)  # начальный баланс
operations = []  # список операций


def check_multiplicity(amount):
    """Проверка кратности суммы"""
    return amount % MULTIPLICITY == 0


def deposit(amount):
    """Пополнение счета"""
    if check_multiplicity(amount):
        global balance
        balance += amount
        operations.append(f"Пополнение карты на {amount} у.е. Итого {balance} у.е.")
    else:
        operations.append(f"Сумма должна быть кратной {MULTIPLICITY} у.е.")


def calculate_removal_percent(amount):
    """Расчет процента на снятие"""
    removal_percent = decimal.Decimal(MIN_REMOVAL) + decimal.Decimal(MAX_REMOVAL - MIN_REMOVAL) * decimal.Decimal(amount / 100000)
    return removal_percent


def withdraw(amount):
    """Снятие денег"""
    global balance
    if check_multiplicity(amount):
        removal_percent = calculate_removal_percent(amount)
        commission = decimal.Decimal(amount) * removal_percent
        if balance < amount + commission:
            operations.append(f"Недостаточно средств. Сумма с комиссией {amount + commission} у.е. На карте {balance} у.е.")
        else:
            balance -= amount
            balance -= commission
            operations.append(
                f"Снятие с карты {amount} у.е. Комиссия {commission} у.е.. Итого {balance} у.е.")
    else:
        operations.append(f"Сумма должна быть кратной {MULTIPLICITY} у.е.")


def exit():
    """Завершение работы и вывод информации о состоянии счета и проведенных операциях"""
    global balance
    if balance > RICHNESS_SUM:
        tax = decimal.Decimal(balance) * decimal.Decimal(RICHNESS_PERCENT) / decimal.Decimal(100)
        balance -= tax
        operations.append(f"Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {tax} у.е. Итого {balance} у.е.")
    operations.append(f"Возьмите карту на которой {balance} у.е.")


# Пример использования
deposit(10000)
withdraw(4000)

exit()

print(operations)