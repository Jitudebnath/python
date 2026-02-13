"""NUmpy array operations(slicing and indexing)"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Basic slicing:", arr[2:7])
print("With step:", arr[1:8:2])
print("Negative indexing:", arr[-3])


arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("specific element:", arr_2d[1, 2])
print("Entire row:", arr_2d[1])
print("Entire column:", arr_2d[:, 1])
