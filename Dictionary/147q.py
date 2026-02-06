"""Store name of a student as key . 'list of 5 marks ' of that student
as a value strore atleast 5 student name.print the sum and percentage
of all the student."""

student_data = {
    "student1": [45, 56, 67, 89, 74],
    "student2": [65, 26, 67, 99, 94],
    "student3": [85, 56, 77, 83, 84],
    "student4": [95, 59, 67, 89, 71],
    "student5": [75, 56, 87, 89, 84],
}
for name, marks in student_data.items():
    total = 0
    for marks in marks:
        total += marks
    percentage = total / 500 * 100
    print(f"{name}has scored total{total}marks,percentage={percentage:.2f}")
