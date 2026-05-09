import numpy as np

arr = np.array([1, np.inf, 3, 4, -np.inf])

print(np.isinf(arr))

"""
Always Remeber That:
-> np.isinf & np.isnan returns Boolean
-> They Both cannot be compare 
-> To Replace them there is single function which is nan_to_num()
"""