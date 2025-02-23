# 10. Write a program to delete an element from the k-th position of an array. 

arr= [1,2,3,4,5,6]
k =int(input(f"Enter the position in limit of {len(arr)} : "))

def del_at_k(arr,k): #array and the position
    # check for valid position
    if k < 0 or k >= len(arr):
        return "Invalid Position"
    
    for i in range(k, len(arr) -1):
        arr[i] = arr[i+1]

    arr.pop()

    return arr


print(f"After deletion at {k}th position: {del_at_k(arr, i)}")
