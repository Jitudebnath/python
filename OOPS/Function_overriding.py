"""polymorphism:Functions overriding"""


class Employee:
    def get_designation(self):
        print("designation=employee")


class Teacher(Employee):
    def get_designation(self):
        print("designation=Teacher")


t1 = Teacher()
t1.get_designation()
