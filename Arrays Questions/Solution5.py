"""
Questions:-

Insert ->
1.Create a 1D array [1, 2, 3, 4] and insert 99 at index 2.
2.Insert 0 at the beginning of an array [5, 6, 7].
3.Insert [10, 20] at index 1 in array [1, 2, 3, 4].
4.Given a 2D array:
arr = [[1,2],[3,4]]
Insert a new row [5,6] at index 1.

Split ->

1. Split [1,2,3,4] into 2 equal parts.
2. Split [10,20,30,40,50] into 5 parts.
"""

# 1. Sol->

import numpy as np

arr = np.array([1,2,3,4])
new_arr = np.insert(arr, 2, 99, axis=None)

print(f"Que 1 Sol->{new_arr}")

# 2. Sol->

arr_02 = np.array([5,6,7])
new_arr_02 = np.insert(arr_02, 0, 0)

print(f"Que 2 Sol->{new_arr_02}")

# 3. Sol->

arr_03 = np.array([1, 2, 3, 4])
new_arr_03 = np.insert(arr_03, 1, [10,20], axis=None)

print(f"Que 3 Sol-> {new_arr_03}")

# 4. Sol->

arr_04 = np.array([[1,2],[3,4]])
new_arr_04 = np.insert(arr_04, 1, [5,6], axis=0)

print(f"Que 4 Sol->\n{new_arr_04}")

# Split 1. Sol->

arr_split = np.array([1, 2, 3, 4])
new_arr_split = np.split(arr_split, 2)

print(f"Split Que 1 Sol-> {new_arr_split}")

# Split 2. Sol->


arr_split_02 = np.array([10,20,30,40,50])
new_arr_split_02 = np.split(arr_split_02, 5)

print(f"Split Que 2 Sol-> {new_arr_split_02}")