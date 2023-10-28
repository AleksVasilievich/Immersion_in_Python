from decimal import Decimal, ROUND_DOWN

MULTIPLICITY = Decimal('100.00')
MIN_REMOVAL = Decimal('0.05')
MAX_REMOVAL = Decimal('0.10')
RICHNESS_SUM = Decimal('10000.00')
RICHNESS_PERCENT = Decimal('0.01')



balance = Decimal('0.00')
operations = []


def check_multiplicity(amount):
    if amount % MULTIPLICITY == 0:
        return True
    return False


def deposit(amount):
    global balance
    if check_multiplicity(amount):
        balance += Decimal(amount)
        operations.append(f"Пополнение карты на {amount} у.е. Итого {balance} у.е.")
    else:
        operations.append(f"Пополнение карты некратно {MULTIPLICITY}: {amount} у.е.")


def withdraw(amount):
    global balance
    if check_multiplicity(amount):
        if amount <= balance:
            commission = amount * (Decimal(MAX_REMOVAL) - Decimal(MIN_REMOVAL))
            balance -= Decimal(amount + commission)
            operations.append(
                f"Снятие с карты {amount} у.е. Процент за снятие {commission} у.е.. Итого {balance} у.е.")
        else:
            operations.append(f"Недостаточно средств на счете: {amount} у.е.")
    else:
        operations.append(f"Сумма снятия некратна {MULTIPLICITY}: {amount} у.е.")


def exit():
    global balance
    if balance > RICHNESS_SUM:
        tax = Decimal(balance * RICHNESS_PERCENT)
        balance -= tax
        operations.append(f"Налог на богатство: {tax} у.е.")
    operations.append(f"Итоговый баланс: {balance} у.е.")
    print(operations)

# def get_operations(self):
#     return self.operations


deposit(10000)
withdraw(4000)
exit()

# operations = get_operations()
#
# for operation in operations:
#     print(operation)