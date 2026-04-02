"""
Split in Nuumpy:-

- np.split() -> Equal to your array
- np.vsplit() -> Vertical Spliting 
- np.hsplit() -> Horizantal Spliting 
"""

import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

print(np.split(arr, 3))
