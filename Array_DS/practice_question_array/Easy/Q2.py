# Reverse an array without using second array 
import array as ar
def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Swap elements
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


arr_temp = ar.array('i', [])
n = int(input("how many numbers? : "))
for i in range(n):
    val = int(input(f"Enter {i+1} element : "))
    arr_temp.insert(i,val)
print(arr_temp)
print(reverse_array(arr_temp))
 
