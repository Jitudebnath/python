"""class in python and a simple example of in python programming language"""


class student:
    college_name = "IGIT,sarang"

    def __init__(self, name, gpa):  # fixed here
        self.name = name
        self.gpa = gpa


stud1 = student("Jitu", 9.2)
stud2 = student("Nihar", 9.7)
stud3 = student("Kedar", 10)
stud4 = student("Khageswar", 9.9)

print(stud1.name, stud1.gpa)
print(stud2.name, stud2.gpa)
print(stud3.name, stud3.gpa)
print(stud4.name, stud4.gpa)
