"""create a bank data and print the name and balance of users"""


class BankAccount:
    def __init__(self, name, balance):
        self.name = name  # public
        self._balance = balance  # private(data mangling)

    def get_balance(self):  # getter
        return self._balance

    def set_balance(self, newBalance):  # setter
        self._balance = newBalance


acc1 = BankAccount("Rahul", 100_000)
acc2 = BankAccount("Nihar", 20_000)

acc1.set_balance(200_000)
print(acc1.name, acc1._balance)
