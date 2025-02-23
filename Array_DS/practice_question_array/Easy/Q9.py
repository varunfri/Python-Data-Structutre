# 9. Write a program to find the binary equivalent of a decimal numbers. 
# find the bin of a num given 

def bin_conv(num):
    bin = ""
    while num >0 :
        bin = str(num % 2) + bin
        num //= 2
    if bin:
        return bin
    else:
        return '0'

n = int(input("Enter a number: "))
print(f"Binary of {n} is {bin_conv(n)}")
