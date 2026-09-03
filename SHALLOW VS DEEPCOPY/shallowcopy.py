import copy

original=[1,2,3]
shallow=copy.copy(original)

print(id(original))
print(id(shallow))

shallow.append(100)

print(original)
print(shallow)