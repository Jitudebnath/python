"""sorting of array"""

import numpy as np

unsorted = np.array([3, 4, 5, 6, 7, 9, 8, 2, 1])
print("sorted:", np.sort(unsorted))

arr_2d_unsorted = np.array([[3, 1], [1, 5], [6, 9]])
print("sorted by row:", np.sort(arr_2d_unsorted, axis=0))
