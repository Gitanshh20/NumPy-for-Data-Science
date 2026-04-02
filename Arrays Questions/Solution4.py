""" 
Bonus Challenge (🔥)
Question->

👉 Create a 3x3 random matrix and: np.random.rand(3,3)
1. Find sum of each row
2. Find sum of each column

Normal Questions:-

3. Using insert function change the elements
4. Now use the append function
5. add two elements
6. Remove the Elements
"""

# Bonus Questions:-

import numpy as np

matrix = np.random.rand(3,3)
print(matrix)

# 1 and 2. => Sum of row wise and column wise:-

Sum_matrix = np.sum(matrix)
print("Total Sum:",round(Sum_matrix, 4))

# 3. Sol=>

arr = np.array([1,2,3,4])
new_arr = np.insert(arr, 0, 5)

print(new_arr)

# 4. Sol=>

arr = np.array([1,2,3,4])
new_arr = np.append(arr, [5,6,7])

print(new_arr)

# 5. Sol=>

arr = np.array([1,2,3])
arr_2 = np.array([4,5,6])

new_arr = np.concatenate((arr,arr_2))

print(new_arr)

# 6. Sol=>

arr = np.array([1,2,3])
remove_arr = np.delete(arr, 2)

print(remove_arr)