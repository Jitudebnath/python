"""Write a program in python to find elements in a given set that
are not in another set"""

set1 = {1, 2, 3, 4, 5, 6}
set2 = {3, 4, 5, 6, 7, 8}

"""result = set()

for i in set1:
    if i not in set2:
        result.add(i)

print(result)
"""

diff = set1 - set2

print(diff)
