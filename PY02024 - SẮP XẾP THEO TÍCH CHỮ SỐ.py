def sum(n):
    res = 1
    while n>0:
        res *= n%10
        n //= 10
    return res
for _ in range(int(input())):
    n = int(input())
    a = list(map(int , input().split()))
    a.sort(key = lambda x : (sum(x),x))
    print(*a)
