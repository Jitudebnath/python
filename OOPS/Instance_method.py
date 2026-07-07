"""Example of Instance_method"""


class laptop:
    storage_type = "SSD"

    def __init__(self, Name, RAM, storage):
        self.Name = Name
        self.RAM = RAM
        self.storage = storage

    def get_info(self):  # Instance_method
        print(
            f"{self.Name} laptop has {self.RAM} RAM & {self.storage} and stoarge type is {self.storage_type}"
        )


l1 = laptop("Lenovo", "16gb", "512gb")
l2 = laptop("Asus", "12gb", "256gb")

l1.get_info()
