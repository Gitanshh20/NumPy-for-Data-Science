
# Vectoriztion Process is 100x faster than Loops

# Vectorization with NumPy ->

import numpy as np

arr1 = np.array([1,2,455,545])
arr2 = np.array([113,12,45325,5453])

print(arr1 + arr2)

# Vectorization with Loops ->

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = [x+y for x,y in zip(list1, list2)]

print(result)