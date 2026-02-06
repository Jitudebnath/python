"""Write a python program to sum all the iteams in
Dictonary"""

marks = {
    "phys": 34,
    "math": 45,
    "computer": 100,
    "history": 67,
}

total = 0
for i in marks.values():
    total = total + i


print(total)
