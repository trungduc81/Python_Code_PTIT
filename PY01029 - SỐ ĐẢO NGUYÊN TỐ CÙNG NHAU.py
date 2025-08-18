import math
t = int(input())
for _ in range(t):
    n = input()
    rev = int(n[::-1])
    n = int(n)
    if math.gcd(rev,n) == 1:
        print("YES")
    else: print("NO")

