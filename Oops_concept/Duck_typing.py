"""polymorphism:duck typing concepts"""

"""polymorphism:Functions overriding"""


class Employee:
    def get_designation(self):
        print("designation=employee")


class Teacher(Employee):
    def get_designation(self):
        print("designation=Teacher")


class Accountant:
    def get_designation(self):
        print("designation=Accountant")


t1 = Teacher()
t1.get_designation()

acc1 = Accountant()
acc1.get_designation()
