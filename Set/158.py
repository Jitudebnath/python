"""GIven two lists a,b check if two lists have at least
one element common in them."""

lst1 = [3, 4, 5, 6, 7, 8, "Nihar"]
lst2 = [5, 6, 7, 8, 9, 0, "Anirudh"]


set1 = set(lst1)
set2 = set(lst2)

# print(set1.intersection(set2))

print(set1 & set2)
print(set1 | set2)
