"""Creating array from scratch"""

import numpy as np

zeros = np.zeros((3, 4))
print("zeros array:\n", zeros)

ones = np.ones((2, 3))
print("ones array:\n", ones)

full = np.full((3, 3), 7)
print("full array:\n", full)

random = np.random.random((2, 3))
print("Random array:\n", random)


sequence = np.arange(0, 10, 2)
print("Sequence array:\n", sequence)
