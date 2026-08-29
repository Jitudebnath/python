"""Here copy method will be discussed in python"""

a = [45, 55, 100, 5, "Jitu debnath", True, 55, 55.556, "code"]
b = a.copy()

print(a)
print(id(a))  # it will gave an id to a list
print(b)
print(id(b))  # same id given to a

a[2] = 0
print(a)
print(b)
