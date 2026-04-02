"""
np.insert(array, index, value, axis=None)

for 2D array:
    axis = 0  rows
    axis = 1 columns
"""

import numpy as np

arr = np.array([1,2,3,4])

print(np.insert(arr, 2 , 3))