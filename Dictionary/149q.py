"""Store the name as key , and 5 marks in a list as a value in dictionary
.Store deatils of at least 5 Students. Print the name of the student who
got higest marks."""

student_data = {
    "student1": [45, 56, 67, 89, 74],
    "student2": [65, 36, 67, 99, 94],
    "student3": [85, 56, 77, 83, 84],
    "student4": [95, 59, 67, 89, 71],
    "student5": [75, 56, 87, 89, 84],
}
highest_marks = 0
highest_student_name = ""

for name, marks in student_data.items():
    total = sum(marks)
    if total > highest_marks:
        highest_marks = total
        highest_student_name = name


print(highest_marks)
print(highest_student_name)
