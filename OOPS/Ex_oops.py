"""1.create a class of a store and save the name of the product
and price of the product.
2.To track the total product being created.
3.Create a static method and claculate the discount on each product in %"""


class Product:
    count = 0

    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"{self.product_name} is {self.price} Ruppes.")

    @classmethod
    def get_count(cls):
        print(f"There are total {cls.count} products in the store.")

    @staticmethod
    def clac_discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"Discounted_price={final_price}")


p1 = Product("Laptop", 40000)
p2 = Product("Mobile", 20000)
p3 = Product("Pen", 10)


p1.get_info()

Product.get_count()

p1.clac_discount(50000, 5)
