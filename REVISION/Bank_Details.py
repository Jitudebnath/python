# write a program for showing the bank deatils in display like take the input from the user and display
class BankAccount:
    def __init__(
        self, bank_name, branch_name, ifc_code, account_no, account_name, balance=0.0
    ):
        self.bank_name = bank_name
        self.branch_name = branch_name
        self.ifc_code = ifc_code
        self.account_no = account_no
        self.account_name = account_name
        self.balance = balance

    def display_account_info(self):
        print("\n----- Account Information -----")
        print(f"Bank Name     : {self.bank_name}")
        print(f"Branch Name   : {self.branch_name}")
        print(f"IFC Code      : {self.ifc_code}")
        print(f"Account No    : {self.account_no}")
        print(f"Account Name  : {self.account_name}")
        print(f"Balance       : {self.balance:.2f}")


# Taking input from user
bank_name = input("Enter Bank Name: ")
branch_name = input("Enter Branch Name: ")
ifc_code = input("Enter IFC Code: ")
account_no = input("Enter Account Number: ")
account_name = input("Enter Account Holder Name: ")
balance = float(input("Enter Initial Balance: "))

# Create object
account = BankAccount(
    bank_name, branch_name, ifc_code, account_no, account_name, balance
)

# Display details
account.display_account_info()
