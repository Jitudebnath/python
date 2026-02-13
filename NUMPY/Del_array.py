"""deleting any element in array"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
deleted = np.delete(arr, 2)
print("Original array", arr)
print("After Delettion of element Array is :", deleted)
