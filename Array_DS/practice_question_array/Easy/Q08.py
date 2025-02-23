# 8. Write a program to find the largest difference in a set of numbers. 
def large_diff(num):
    min_val = max_val = num[0]

    for x in num:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x

        diff = max_val - min_val
    return diff

import array as arr
ar = arr.array('i', [1,2,3,4,5])
print("Largest diff : ", large_diff(ar))
