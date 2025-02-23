def prod_except(arr):
    n = len(arr)
    result = [1] * n   
 
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:   
                product *= arr[j]
        result[i] = product

    return result


arr = [1, 2, 3, 4,5]
print("Output:", prod_except(arr))
