"""Array compatibility"""

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6, 8])
arr3 = np.array([7, 8, 9])

print("Compatibility array", arr1.shape == arr2.shape)
