# Create a function to remove the duolicated in array using set and loops

arr_2 = arr.array('i',[11,11,12,2,2,12,11,13,13,3,3])

def remove_dup(x):
    lis= []
    # for i in x:
    #     if i in lis:
    #         continue
    #     else:
    #         lis.append(i)

    for i in x:
        if i not in lis:
            lis.append(i)
    return arr.array('i',lis)

def use_set(x):
    # convert to set 
    set_x = set(x)
     
    return arr.array("i",set_x)

print("Removed duplicates using loops: ",remove_dup(arr_2))
print("removed duplicates usign the set: ",use_set(arr_2))
