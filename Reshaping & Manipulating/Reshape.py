"""
It's Use to change the dimesion of an array.
Example:
1D -> 2D
2D -> 3D

Synatx:

reshape(rows, columns)

"""

import numpy as np

arr = np.array([1, 2, 3, 4]) 

print(arr.reshape(2,2))