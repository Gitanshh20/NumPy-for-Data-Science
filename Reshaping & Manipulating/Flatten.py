"""
.ravel() -> Original Array affected
.flaten() -> Affect Copy of Array

"""

import numpy as np

arr = np.array([[1, 2], [3, 4], [5,6]]) 

print(f"{arr}\n")

print(arr.flatten())
print(arr.ravel())