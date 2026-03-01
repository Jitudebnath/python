"""static method Example in python programming language"""


class laptop:
    storage_type = "SSD"

    def __init__(self, Name, RAM, storage):
        self.Name = Name
        self.RAM = RAM
        self.storage = storage

    def get_info(self):
        print(
            f"{self.Name} laptop has {self.RAM} RAM & {self.storage} and stoarge type is {self.storage_type}"
        )

    @staticmethod  # static_method
    def clac_discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"Discounted_price={final_price}")


l1 = laptop("Lenovo", "16gb", "512gb")

product_price = int(input("Enter the product price:"))
Given_discount = int(input("Enter the discount in %:"))

l1.clac_discount(product_price, Given_discount)
l1.get_info()
