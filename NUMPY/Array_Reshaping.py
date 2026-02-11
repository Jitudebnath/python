"""Array Reshaping"""

import numpy as np

arr = np.arange(12)
print("Original array", arr)

reshaped = arr.reshape((3, 4))
print("Reshaped array:", reshaped)

flattened = reshaped.flatten()
print("\n flattened array", flattened)

# Revel (return view instead of copy)
reveled = reshaped.ravel()
print("\n reveled array ", reveled)

# transpose
transpose = reshaped.T
print("\n Transposed array ", transpose)
