"""
Questions:- 

1. Access the 3rd element of an array.
2. Slice elements from index 2 to 5.
3. Reverse an array.
4. Find the shape and size of an array.

"""

# 1. Solution:- 

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(f"3rd Elements = {arr[2]}")

# 2. Solution:- 

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(f"Slicing from 2 to 5 = {arr[2:6]}")

# 3. Solution:- 

arr = np.array([1, 2, 3, 4, 5])

print(f"Revesred Array = {arr[::-1]}")

# 4. Solution:- 

arr = np.array([1, 2, 3, 4, 5])

print(f"This is Your Array's Shape = {arr.shape}")
print(f"This is Your Array's Size = {arr.size}")