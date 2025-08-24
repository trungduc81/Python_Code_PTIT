import math
def check(n):
    sum = 0
    k = n
    while n>0:
        sum += math.factorial(n%10)
        n //= 10
    return sum == k

t = int(input())
for _ in range(t):
    n = int(input())
    if check(n): print("Yes")
    else : print("No")
