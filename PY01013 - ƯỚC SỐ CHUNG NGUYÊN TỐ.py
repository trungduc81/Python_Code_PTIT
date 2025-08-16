import math

def isprime(n):
    if n<2: return False
    for i in range(2,(int)(math.sqrt(n))+1):
        if n%i ==0: return False
    return True

def tong(n):
    sum = 0
    while n>0:
        sum += n%10
        n //= 10
    return sum

t = int(input())
while t>0:
    a , b = map(int,input().split())
    gcd = math.gcd(a,b)
    if(isprime(tong(gcd))) : print("YES")
    else: print("NO")
    t -= 1
