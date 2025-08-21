t = int(input())
for _ in range(t):
    n = int(input())
    res = 1
    while n>0:
        m = n % 10
        if m != 0 : res *= m
        n //= 10
    print(res)

