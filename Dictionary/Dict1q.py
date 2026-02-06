"""This is the concept of dictionary in"""

student_data = {
    "Jitu": {
        "roll_number": 21,
        "gender": "male",
        "marks": [92, 99, 89],
    },
    "Nihar": {
        "roll_number": 29,
        "gender": "male",
        "marks": [90, 90, 90],
    },
    "Khageswar": {
        "roll_number": 35,
        "gender": "male",
        "marks": [85, 90, 85],
    },
}

for name, details in student_data.items():
    total = 0
    for mark in details["marks"]:  # iterate through marks list
        total += mark  # add each mark to total
    print(f"{name} has {total} marks")
