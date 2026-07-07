"""Talking about the different type of methods
which are present in the list"""

a = [12, 232, 45, 56, 78, 89, 56, 12]
pos = a.index(89)
print(pos)  # print position using index value
a.sort()  # Ascending
print(a)
a.reverse()  # Descending
print(a)  # sorting the value in asending order
r = a.count(12)
print(r)
