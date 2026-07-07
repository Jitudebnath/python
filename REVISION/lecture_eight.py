class Student:
    name = "jitu debnath"


# class realated this one
class Car:
    color = "blue"
    brand = "TATA motors"


car = Car()

print(Car.color)
print(Car.brand)


# this program is all about constructor in python
class Std:

    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in Database..")


s1 = Std("karan")
print(s1.name)

s2 = Std("arjun")
print(s2.name)


# this program  is all about the class and some of its features
class Student:
    college_name = "ABC college"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student")

        s1 = Student("Jitu debnath", 97)
        s1.welcome()
