"""inheritance concepts"""


class Animal:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def eat(self) -> None:
        print("I am eating")

    def sleep(self) -> None:
        print("I am sleeping")


class Dog(Animal):

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print("I am barking")

    def display(self):
        print(f"My name is {self.name} and age is {self.age}")


dog = Dog("puppy", 6, "germanshepard")
dog.display()
