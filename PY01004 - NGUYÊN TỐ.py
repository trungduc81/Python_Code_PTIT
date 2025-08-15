import math

def isprime(n) :
    if n<2:
        return 0
    for i in range(2,(int)(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1

t =int(input())
for i in range(t):
    cnt = 0
    n = int(input())
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            cnt += 1
    if (isprime(cnt)):
        print("YES")
    else:
        print("NO")



