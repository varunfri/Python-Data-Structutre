# Rotate an array from kth position

def rotate_array(arr, k):
    n = len(arr)
    if k > n:
      return f"Max range is {n}"

    # function to reverse a portion of the array
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Step 1: Reverse the entire array
    reverse(0, n - 1)

    # Step 2: Reverse first k elements
    reverse(0, k - 1)

    # Step 3: Reverse remaining elements
    reverse(k, n - 1)

    return arr  # In-place modification

arr = [1, 2, 3, 4, 5]
k = 2
print("Output:", rotate_array(arr, k))
