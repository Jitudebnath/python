"""
Write a program that has two list and make a new list that contains
only the common elements between them without dupliicates
"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [5, 6, 7, 8, 9, 1]

result = []

for i in list1:
    if i in list2:
        if i not in result:
            result.append(i)


print(f"First list is ={list1}")
print(f"The second list is ={list2}")
print(f"The resultant list is ={result}")
