"""
How To Replace the value of isinf and isnan?
-> We can Replace the value of np.isinf and np.isnan with the np.nan_to_num

1. For isnan 
-> Synatx:- np.nan_to_num(array, nan=value)  

2. For isinf 
-> Synatx:- np.nan_to_num(array, posinf=value, neginf=value) 
"""

import numpy as np

inf = np.array([1, np.inf, 3, -np.inf, 5]) 
nan = np.array([1, np.nan, 3, np.nan, 5]) 

print(np.isinf(inf),np.isnan(nan))

cleaned_inf = np.nan_to_num(inf, posinf=2, neginf=-4)
cleaned_nan = np.nan_to_num(nan, nan=2)

print(f'inf = {cleaned_inf}\nnan = {cleaned_nan}')