#  Write a program to find the smallest element among N inputted numbers. 
import numpy as np
def find_small_n(arr):
    small = arr[0]
    for num in arr:
        if num < small:
            small = num
    return small

arr_temp = []
n = int(input("How many number want to enter? : "))
for i in range(n):
    val = int(input(f"Enter {i+1} element: "))
    arr_temp.append(val)
arr_n = np.array(arr_temp)
print(arr_n)

print("Smallest among N numbers is: ",find_small_n(arr_n))
