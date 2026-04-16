"""Adding new row and col in array in python"""

import numpy as np

original = np.array([[1, 2], [3, 4]])
new_row = np.array([[5, 6]])

# Add a new row
with_new_row = np.vstack((original, new_row))
print("Original:\n", original)
print("With new row:\n", with_new_row)

# Add a new column
new_col = np.array([[7], [8]])
with_new_col = np.hstack((original, new_col))
print("With new column:\n", with_new_col)
