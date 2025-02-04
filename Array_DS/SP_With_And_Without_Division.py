# Array special product, with division and without division
import array as arr

x = arr.array("i",[1,2,3,4,5])

def SP_without_division(x):
    n = len(x)
    res = [1] *n
    for i in range(n):
        for j in range(n):
            if i != j:
                res[i] *= x[j]
    return res

SP_without_division(x)

def SP_With_division(x):
    res = []
    # use math lib total = math.prod(x), directly use for j in x: val = total//j res.append(val) return res
    total = 1
    for i in x:
        total *= i
    print(total)
    
    for j in x:
        val = total//j
        res.append(val)

    return res

SP_With_division(x)
