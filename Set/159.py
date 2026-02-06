"""Common element in three lists using sets"""

lst1 = [3, 4, 5, 6, 7, 8, 9, "python", "jitu"]
lst2 = [7, 8, 9, 5, 6, 8, 2, "Balaram"]
lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

set1 = set(lst1)
set2 = set(lst2)
set3 = set(lst3)


print(f"common elements are {set1 & set2 & set3}")
