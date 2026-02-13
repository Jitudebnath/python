"""Adding new row and col in array in python"""

import numpy as np

original = np.array([[1, 2], [3, 4]])
new_row = np.array([[5, 6]])

with_new_row = np.vstack((original, new_row))
print(original)
print(with_new_row)


new_col = np.array([[7], [8]])
with_new_col = np.hstack((original, new_row))
print(with_new_col)
