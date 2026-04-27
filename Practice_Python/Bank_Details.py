class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}deposited sucessfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Account Holder: {self.name}, Balance: {self.balance}")


print("-----Bank_Details-----")
account1 = BankAccount("Jitu", 1000)
account1.display_balance()
account1.deposit(500)
account1.withdraw(300)
account1.withdraw(1500)  # should show insufficient funds
account1.display_balance()
