"""Filtering of array in python using numpy"""

import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even_number = numbers[numbers % 2 == 0]
print("Even numbers", even_number)


##FILTER WITH MARK
mask = numbers > 5
print("Numbers greater than 5", numbers[mask])


# FANCY INDEXING VS NP.WHERE()
indices = [0, 2, 4]
print(numbers[indices])
where_result = np.where(numbers > 5)
print("NP where", numbers[where_result])

condition_array = np.where(numbers > 5, numbers * 1, numbers)
print(condition_array)
