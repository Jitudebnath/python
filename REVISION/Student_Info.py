"""print the name,roll_no,marks"""


class student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def display_details(self):
        avg = self.calculate_average()
        status = "pass" if avg > 60 else "Fail"
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Average Marks: {avg:.2f}")
        print(f"Result: {status}")


student1 = student("Jitu", 101, [50, 60, 70])
student2 = student("Ravi", 102, [30, 25, 35])


print("-----Student_Deatils------")
print("Student 1")
student1.display_details()
print()
print("Student 2")
student2.display_details()
print()
