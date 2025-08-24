import math
def prime(n) :
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True

def check(n):
    if not prime(n) : return False
    m = str(n)
    rev = m[::-1]
    if not prime(int(rev)) : return False
    sum = 0
    while n>0:
        k = n%10
        if not prime(k): return False
        sum += k
        n //= 10
    return prime(sum)

t = int(input())
for _ in range(t):
    n = int(input())
    if check(n): print("Yes")
    else : print("No")
