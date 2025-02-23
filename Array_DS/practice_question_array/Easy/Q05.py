# Find the largest odd number

x = [1,2,3,4,5,6,7,8,9,11,13,17, 52] #1,3,5,7,9,11,13,17


def large_odd(num):
    large = 0

    for x in num:
       if x % 2 != 0:
         large < x
         large = x
    return large


print("Largest Odd number is: ", large_odd(x))
