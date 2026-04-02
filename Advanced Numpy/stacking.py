"""
For Stacking Numpy have two methods which are :-
1. vstack() -> Vertical Stacking
2. hstack() -> Horizntal Stacking

"""

import numpy as np

arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6])

print(f"Verticaly Stacking:-\n{np.vstack((arr_1,arr_2))}")
print(f"Horizantly Stacking:-\n{np.hstack((arr_1,arr_2))}")