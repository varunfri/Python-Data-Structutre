# Write a program to insert an element at its proper position in a previously sorted array.  
def insert_sorteds(arr, new_element):
    n = len(arr)
    arr.append(0)  # increase array by 1 elem
    
    i = n - 1
    while i >= 0 and arr[i] > new_element:  # Shift elements right
        arr[i + 1] = arr[i]
        i -= 1
    
    arr[i + 1] = new_element  # Insert the new element
    
    return arr

arr = [10, 20, 30, 40, 50] 
new_element = 25
print("Updated Array:", insert_sorted(arr, new_element))
