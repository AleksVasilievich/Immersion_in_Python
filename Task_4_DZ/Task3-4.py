import decimal

MULTIPLICITY = 50  # множитель, кратность суммы
MIN_REMOVAL = 0.5  # минимальная комиссия за снятие в процентах
MAX_REMOVAL = 15  # максимальная комиссия за снятие в процентах
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
    if amount <= 1000:
        return (decimal.Decimal(amount) / 100) * decimal.Decimal(MAX_REMOVAL)
    elif amount <= 10000 and amount > 1000:
        return (decimal.Decimal(amount) / 100) * decimal.Decimal(MAX_REMOVAL) * 10
    # elif amount <= 3000:
    #     return decimal.Decimal(amount) * (decimal.Decimal(MAX_REMOVAL) + decimal.Decimal(10)) / decimal.Decimal(100)
    else:
        return decimal.Decimal(amount) * (decimal.Decimal(MAX_REMOVAL) + decimal.Decimal(15)) / decimal.Decimal(100)


def withdraw(amount):
    """Снятие денег"""
    global balance
    if check_multiplicity(amount):
        removal_percent = calculate_removal_percent(amount)
        if balance < amount + removal_percent:
            operations.append(f"Недостаточно средств. Сумма с комиссией {amount + removal_percent} у.е. На карте {balance} у.е.")
        else:
            balance -= amount
            balance -= removal_percent
            operations.append(
                f"Снятие с карты {amount} у.е. Процент за снятие {removal_percent} у.е.. Итого {balance} у.е.")
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
deposit(1000)
withdraw(200)
exit()

print(operations)

deposit(1000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()

print(operations)