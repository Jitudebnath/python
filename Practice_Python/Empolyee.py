class Employee:
    # Attributes
    """name = ""
    age = 0
    gender = ""
    address ="""

    # Methods
    def set_info(self):
        self.name = input("Enter your name :")
        self.age = int(input("Enter your age :"))
        self.gender = input("Enter your gender :")
        self.address = input("Enter the address :")

    def display(self):
        print(
            f"My name is {self.name},age is {self.age} and gender is {self.gender} and my adress is {self.address}."
        )


e1 = Employee()
e1.set_info()
e1.display()
