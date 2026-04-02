"""
np.concatenate((array1,array2), axis = 0)

axis 0 -> Rows or Vertical
axis 1 -> Columns or Horizontal
"""

import numpy as np

arr1 = np.array([1,2])
arr2 = np.array([3,4])

new_arr = np.concatenate((arr1,arr2), axis=0)

print(new_arr)