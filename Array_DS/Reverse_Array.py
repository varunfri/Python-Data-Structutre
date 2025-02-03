# Create a function to return reversed array 

import array as arr
arr_1 = arr.array([1,32,4,5,61])

print("Array reverse using the slice:\n",arr_1[::-1])

def rev_array(x):
    n = len(x)
    lis_1= []
    print("Reverse array using the loops: ")
    for i in range(n-1, -1,-1):
        lis_1.append(arr_1[i])
    
    return arr.array('i',lis_1)

print(rev_array(arr_1))
