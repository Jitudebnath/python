import copy

original=[1,2,3,[23,34,45],56,67,78]
shallow=copy.copy(original)

print(id(original))
print(id(shallow))

shallow[3][1] = 999
shallow[6] = 1000

print(original)
print(shallow)