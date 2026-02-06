"""This is the concept of dictionary in"""

student_data = {
    "Jitu": {
        "roll_number": 21,
        "gender": "male",
        "physics": 89,
        "chemistry": 78,
        "mathematics": 96,
    },
    "Nihar": {
        "roll_number": 29,
        "gender": "male",
        "physics": 89,
        "chemistry": 88,
        "mathematics": 91,
    },
    "Khageswar ": {
        "roll_number": 35,
        "gender": "male",
        "physics": 95,
        "chemistry": 78,
        "mathematics": 90,
    },
}
# print(student_data["Jitu"]["roll_number"])
# print(student_data["Nihar"]["chemistry"])

for name, deatils in student_data.items():
    print(name)
    print(deatils["physics"])
