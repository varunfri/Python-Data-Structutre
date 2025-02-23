# 7. Find the second highest element among N inputted numbers
def second_highest(numbers):
    if len(numbers) < 2:
        return "Not enough elements"

    highest = second_highest = float('-inf')  # Initialize to very small values

    for num in numbers:
        if num > highest:  # New highest found
            second_highest = highest  # Move highest to second highest
            highest = num  # Update highest
        elif num > second_highest and num != highest:  # Update second highest
            second_highest = num

    return second_highest if second_highest != float('-inf') else "No second highest"

# Example usage
num_list = [10, 20, 4, 45, 99, 99, 23]
print("Second Highest Number:", second_highest(num_list))
