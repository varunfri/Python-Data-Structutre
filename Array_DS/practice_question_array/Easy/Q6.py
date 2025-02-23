# 6. Count the total number of prime numbers in a set of integers
# Prime => The number which is divisible by 1 and itself is called as prime > 1 ( start from 2 .....)

def count_primes(numbers):
    count = 0
    for x  in numbers:
        if x < 2:
            continue  # Ignore numbers less than 2
        is_prime = True
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                is_prime = False
                break  # No need to check further if it's already non-prime
        if is_prime:
            count += 1
    return count

# Example usage
num_set = [10, 11, 13, 15, 17, 19, 21, 23, 29, 31]
print("Prime Numbers are :", count_primes(num_set))
