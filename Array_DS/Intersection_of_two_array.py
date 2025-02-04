import array as arr

arr_1 = arr.array('i', [1,2,3,4,5,6])
arr_2 = arr.array('i',[1,2,3,44,5,6,])

def commn_data(x,y):
    new_arr= []
    for i in x:
        if i in y:
            new_arr.append(i)
        
    return arr.array('i', new_arr)

commn_data(arr_1, arr_2)


