# Write a function to get sum and avg of array

import numpy as np

def sum_avg(x):
    sum = x.sum()
    avg = sum/(len(x))
    return sum, avg
arr_np = np.array([1,2,33,44,4,5])
print(sum_avg(arr_np))
