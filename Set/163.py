"""Write a python program to check if two given
sets have no elemets in common"""

set1 = {1, 2, 3, 4, 5, 6}
set2 = {3, 4, 5, 6, 7, 8}

result = set1.intersection(set2)

if len(result) == 0:
    print("No common elements are there.")
else:
    print(f"{result} these are common elements. ")
