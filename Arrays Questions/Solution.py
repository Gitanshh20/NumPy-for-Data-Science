'''
Questions:-

1. Create a NumPy array from a Python list [1, 2, 3, 4, 5].
2. Create an array of all zeros with size 5.
3. Create an array of all ones with shape (3, 3).
4. Generate numbers from 0 to 10 using arange()

'''

# 1. Solution :-
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(f"This is Your Array = {arr}")

# 2. Solution :- 

arr = np.zeros(5)

print(f"This is Your Zeros with the size of 5 = {arr}")

# 3. Solution:- 

arr = np.ones((3,3))

print(f"This is Your array with ones and shape also 3,3:-\n{arr}")

# 4. Solution:- 

arr = np.arange(0, 11)

print(f"This is Your Array start form 0 and end with 10 = {arr}")
