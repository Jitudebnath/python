"""multiply two matrices using python programming language"""

# Matrix Multiplication in Python

# Take dimensions of matrices from user
rows_A = int(input("Enter number of rows in Matrix A: "))
cols_A = int(input("Enter number of columns in Matrix A: "))

rows_B = int(input("Enter number of rows in Matrix B: "))
cols_B = int(input("Enter number of columns in Matrix B: "))

# Check if multiplication is possible
if cols_A != rows_B:
    print("Matrix multiplication not possible! (columns of A must equal rows of B)")
else:
    print("\nEnter elements of Matrix A:")
    A = []
    for i in range(rows_A):
        row = []
        for j in range(cols_A):
            val = int(input(f"A[{i}][{j}] = "))
            row.append(val)
        A.append(row)

    print("\nEnter elements of Matrix B:")
    B = []
    for i in range(rows_B):
        row = []
        for j in range(cols_B):
            val = int(input(f"B[{i}][{j}] = "))
            row.append(val)
        B.append(row)

    # Initialize result matrix with zeros
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    # Display result
    print("\nResultant Matrix (A × B):")
    for row in C:
        print(row)
