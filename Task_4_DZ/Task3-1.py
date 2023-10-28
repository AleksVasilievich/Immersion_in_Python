from decimal import Decimal, ROUND_DOWN

MULTIPLICITY = Decimal('100.00')
MIN_REMOVAL = Decimal('0.05')
MAX_REMOVAL = Decimal('0.10')
RICHNESS_SUM = Decimal('10000.00')
RICHNESS_PERCENT = Decimal('0.01')

class BankAccount:
    def __init__(self):
        self.balance = Decimal('0.00')
        self.operations = []

    def check_multiplicity(self, amount):
        if amount % MULTIPLICITY == 0:
            return True
        return False

    def deposit(self, amount):
        if self.check_multiplicity(amount):
            self.balance += Decimal(amount)
            self.operations.append(f"Пополнение карты на {amount} у.е. Итого {self.balance} у.е.")
        else:
            self.operations.append(f"Пополнение карты некратно {MULTIPLICITY}: {amount} у.е.")

    def withdraw(self, amount):
        if self.check_multiplicity(amount):
            if amount <= self.balance:
                commission = amount * (Decimal(MAX_REMOVAL) - Decimal(MIN_REMOVAL))
                self.balance -= Decimal(amount + commission)
                self.operations.append(f"Снятие с карты {amount} у.е. Процент за снятие {commission} у.е.. Итого {self.balance} у.е.")
            else:
                self.operations.append(f"Недостаточно средств на счете: {amount} у.е.")
        else:
            self.operations.append(f"Сумма снятия некратна {MULTIPLICITY}: {amount} у.е.")

    def exit(self):
        if self.balance > RICHNESS_SUM:
            tax = Decimal(self.balance * RICHNESS_PERCENT)
            self.balance -= tax
            self.operations.append(f"Налог на богатство: {tax} у.е.")
        self.operations.append(f"Итоговый баланс: {self.balance} у.е.")

    def get_operations(self):
        return self.operations

# Пример использования

account = BankAccount()

account.deposit(10000)
account.withdraw(4000)
account.exit()

operations = account.get_operations()

for operation in operations:
    print(operation)