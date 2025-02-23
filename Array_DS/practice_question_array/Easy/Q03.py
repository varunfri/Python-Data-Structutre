# 3. Find Standard Deviation of N numbers

def standard_deviation(numbers):
    n = len(numbers)
    sumn = 0
    for x in numbers:
        sumn += x
    print(f"Sum of numbers: {sumn}")

    # find the mean 
    mean = sumn/n 
    print(f"Mean is : {mean}")

    # find the (x-mean)^2 of each element and store it
    square_diff = []
    for x in numbers:
        res = (x-mean) ** 2
        square_diff.append(res)

    print("Squared Diff of numbers: ", square_diff)

    # find the sum(squared_diff)
    sum_square_diff = 0
    for x in square_diff:
        sum_square_diff += x

    print("Sum of squared diff is: ", sum_square_diff)

    # Variance = sum(squared_diff)/n
    variance = sum_square_diff/n
    print(f"Variance: {variance}")

    # standard deviation is sqrt(variance) or variance ** 0.5

    std = variance ** 0.5
    return std


num = [10, 12, 23, 23, 16, 23, 21, 16]
res = standard_deviation(num)
print(f"Standard Deviation is: {res}")

