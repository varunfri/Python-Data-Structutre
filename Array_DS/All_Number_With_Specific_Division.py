# All numbers with specific division
N= 13; D=2; low = 1; high =13

while low<=high:
    mid = (high+low)//2
    sum_d= sum(int(digit) for digit in str(mid))
    diff = mid-sum_d
    if abs(diff) <=2:
        low = mid+1
    else :
        high = mid-1 
print(N-high)
