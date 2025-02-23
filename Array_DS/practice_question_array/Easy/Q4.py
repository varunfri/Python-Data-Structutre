#4. Write a program to count odd numbers in a set of integers. 
def count_odd(nums):
    count = 0
    for x in nums:
        if x % 2 != 0:
            count += 1
    return count

x = [1,2,3,4,5,6,7,8,9,11,13,17] #1,3,5,7,9,11,13,17
print("Odd Count is: ", count_odd(x))

