"""using python understading encapculation with a bank realted example"""


class Bank:
    def __init__(self, name: str, balance: int):
        self.name = name
        self.__balance = balance

    print("-----Transaction Details-----")

    def get_balance(self):
        print(f"current balance {self.__balance}")

    def deposit(self, amount: int) -> int:
        self.__balance += amount
        print(f"Amount deposited,current balance is {self.__balance}")

    def withdraw(self, amount) -> int:
        if amount > self.__balance:
            print("Not enough money in the bank\n")
        else:
            self.__balance -= amount
            print(f"Amount withdrawn,current balance is {self.__balance}\n")


acc = Bank("Jitu Debnath", 20000)
acc.deposit(100)
acc.get_balance()
acc.withdraw(7898)
