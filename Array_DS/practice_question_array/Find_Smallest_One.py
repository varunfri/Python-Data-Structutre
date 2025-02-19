# Write a program to find the smallest element among N inputted numbers.

n = int(input("Enter the number of elements: "))  

if n <= 0:
    print("Invalid input! The number of elements must be greater than 0.")
else:
    arr = []  # Initialize an empty list

    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        arr.append(num)  # Store numbers in the list

    smallest = arr[0]  # Assume the first element is the smallest

    for i in range(1, n):
        if arr[i] < smallest:  # Compare each element with smallest
            smallest = arr[i]

    print("The smallest number is:", smallest)
