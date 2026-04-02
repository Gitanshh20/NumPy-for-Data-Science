
import numpy as np

arr_2D = np.array([[1,2],[3,4]])

new_arr_2D = np.insert(arr_2D, 2, [5,6], axis=0)

print(new_arr_2D)