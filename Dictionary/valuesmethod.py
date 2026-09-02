"""values method using python programming language"""

marks={
    "science":98,
    "mathematics":99,
    "computer":99,
    "hindi":90,
    "history":71,
}
total = 0
for mark in marks.values():
    total +=mark

print(f"total marks is ",total)