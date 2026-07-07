"""Example of inheritance in python
which is an core concepts of oops"""


class Employee:
    Start_time = "10pm"
    End_time = "4pm"


class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject


t1 = Teacher("Mathematics")

print(f"Teacher subject is ", t1.subject, "and entry time is", t1.Start_time)
