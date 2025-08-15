import math

t = int(input())
while t>0:
    n , x , m = map(float,input().split())
    cnt = 0
    while n < m:
        n = n + x*n/100
        cnt += 1
    print(cnt)
    t = t - 1
