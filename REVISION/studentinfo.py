class Student:
    # using constructor/initilizer
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def display(self) -> None:
        print(f"My name is {self.name},age is {self.age} and gender is {self.gender}.")


s1 = Student("jitu", 22, "male")
s1.display()
