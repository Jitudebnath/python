"""Difference between list and array"""

import numpy as np
import time

py_list = [1, 2, 3]  # 2 times in list
print("python list multiplication", py_list * 2)

np_array = np.array([1, 2, 3])  # element wise multplication
print("python array multiplication", np_array * 2)


start = time.time()
py_list = [i * 2 for i in range(1000000)]
print("\n list operation time:", time.time() - start)

start = time.time()
np_array = np.arange(1000000) * 2
print("\n Numpy operation time:", time.time() - start)
