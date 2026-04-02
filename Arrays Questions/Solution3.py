"""
Questions:-

1.Create a 3×3 matrix with random values.
2.Add two arrays element-wise.
3.Multiply two arrays (element-wise and matrix multiplication).
4.Find the maximum and minimum value in an array.
5.Calculate mean, median, and standard deviation.
6.Use boolean indexing to filter values greater than 10.
7.Flatten a 2D array into 1D.

"""
# 1. Solution:-

import numpy as np
import random

matrix = np.random.rand(3,3)

print(matrix)

# 2. Solution:- 

arr = np.array([1, 2, 3, 4])
arr_2 = np.array([1, 2, 3, 4]) 

print(f"This is Your Sum = {arr + arr_2}")

# 3. Solution:- 

matrix = np.array([[1, 2, 3, 4],[1, 2, 3, 4]])
matrix_2 = np.array([[1, 2, 3, 4],[1, 2, 3, 4]]) 

print(f"This your Ans:\n{matrix*matrix_2}")

# 4. Solution:- 

arr = np.min([1,453,565,213,57])
arr_2 = np.max([1,453,565,213,57])

print(f"This is Minimum value of an array: {arr}")
print(f"This is Maximum value of an array: {arr_2}")

# 5. Solution:- 

arr_mean = np.mean([1,2,3,4,5])
arr_median = np.median([1,2,3,4,5])
arr_std = np.std([1,2,3,4,5])

print(f"Mean = {arr_mean}")
print(f"Median = {arr_median}")
print(f"Standard devation = {arr_std}")

# 6. Solution:-

arr = np.array([55,66,44,1,2,3,4])

print(arr[arr > 10])

# 7. Solution:-

arr = np.array([[1,2,3],[4,5,6]])

print(arr.flatten())