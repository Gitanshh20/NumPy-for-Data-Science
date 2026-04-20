import numpy as np

arr1 = np.array([[1,2,3],[4,5,6]]) # Shape (2,3)
arr2 = np.array([1,2]) # Shape (2,)

result = arr1 + arr2

print(result) # Output: ValueErorr Means that it will be not added.

# Solution of this ->
"""
You can do np.append() here
"""

import numpy as np

arr1 = np.array([[1,2,3],[4,5,6]]) # Shape (2,3)
arr2 = np.array([1,2]) # Shape (2,)

new_arr2 = np.append(arr2 , [3])

result = arr1 + new_arr2

print(result)