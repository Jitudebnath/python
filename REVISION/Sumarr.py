import numpy as np

n = int(input("Enter size of arrays: "))

a = np.zeros(n, dtype=int)
b = np.zeros(n, dtype=int)

print("Enter elements for first array:")
for i in range(n):
    a[i] = int(input())

print("Enter elements for second array:")
for i in range(n):
    b[i] = int(input())

sum_array = a + b

print("First array:", a)
print("Second array:", b)
print("Sum:", sum_array)


