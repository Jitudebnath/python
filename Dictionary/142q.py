"""Ask subject and marks from the user and
keep adding it to dictionary."""

marks = {}
subject_count = int(input("Enter the numbers of subjects:"))
total = 0

for _ in range(0, subject_count):
    subject_name = input("Enter subject:")
    subject_marks = int(input(f"Marks of {subject_name}:"))
    marks[subject_name] = subject_marks
    total = total + 1

    print(marks)
