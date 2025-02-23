# Move all Zeros to end 
def move_zero(arr):

    n = len(arr)
    j = 0

    for i in range(n):
        print(i, j)
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
            print(arr)
            

    return arr

ar = [0,1,0,3,0]
print("After Moving all zero to end: ", move_zero(ar))
