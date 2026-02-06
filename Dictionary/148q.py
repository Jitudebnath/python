"""Store marks of 5 different subjects in a dictonary . Ask
subject name as an input from the user . print the marks of that
subject entered by the user. if subject does not exist, print 'invalid'"""

subject_marks_dict = {
    "math": 90,
    "English": 85,
    "science": 92,
    "History": 89,
    "Computer_science": 95,
}

subject_name = input("Enter the subject name:")

if subject_name in subject_marks_dict:
    print(subject_marks_dict[subject_name])
else:
    print("INVALID")
