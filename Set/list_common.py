"""list common in python"""

a = [3, 4, 5, 6, 7, 8]
b = [3, 5, 68, 91, 45]

c = set(a)
d = set(b)

result = list(c.intersection(d))
print(result)
