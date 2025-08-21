import math

def check(n):
    pri , not_pri = 0 , 0
    scs = 0
    while n>0:
        if isprime(n%10): pri += 1
        else: not_pri += 1
        scs += 1
        n //= 10
    return pri > not_pri and isprime(scs)

def isprime(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i ==0 : return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    if check(n): print("YES")
    else : print("NO")

