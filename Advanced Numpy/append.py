"""
Append:-
np.append(array, value)

=> Value come out in end of the array.
"""

import numpy as np

arr = np.array([1,2,3,4])
new_arr = np.append(arr, [5,6,7])

print(new_arr)