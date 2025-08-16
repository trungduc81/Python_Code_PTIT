a, k, n = map(int, input().split())
tmp = k
check = False
while k <= n:
    if k - a > 0:
        print(k - a, end=" ")
        check = True
    k += tmp

if not check:
    print(-1)
