# Multiplication Table with Numpy

import numpy as np

n = int(input("Enter Your Number:- "))

arr = np.arange(n, n*11, n)

print(f"Table:- {arr}")
