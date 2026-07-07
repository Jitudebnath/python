"""matrix multplication using python programming language"""

# Matrix Addition in Python

# Take matrix dimensions from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter elements of Matrix A:")
A = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"A[{i}][{j}] = "))
        row.append(val)
    A.append(row)

print("\nEnter elements of Matrix B:")
B = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"B[{i}][{j}] = "))
        row.append(val)
    B.append(row)

# Perform matrix addition
C = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)

# Display result
print("\nResultant Matrix (A + B):")
for row in C:
    print(row)
