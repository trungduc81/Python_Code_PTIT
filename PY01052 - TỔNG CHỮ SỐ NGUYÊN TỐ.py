import math
def isprime(n):
    if n<2: return False
    for i in range(2,(int(math.sqrt(n))+1)):
        if n%i==0: return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    sum = 0
    while n>0:
        sum += n%10
        n //= 10
    if isprime(sum):print("YES")
    else : print("NO")

