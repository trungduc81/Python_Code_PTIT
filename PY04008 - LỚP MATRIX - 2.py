import sys

data = list(map(int, sys.stdin.read().split()))
t = data[0]
idx = 1
for _ in range(t):
    n, m = data[idx], data[idx+1]
    idx += 2
    a = []
    for i in range(n):
        tmp = data[idx: idx+m]
        a.append(tmp)
        idx += m
    rev = list(map(list, zip(*a)))  # zip(*matrix) để chuyển vị
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(m):
                res[i][j] += a[i][k] * rev[k][j]
    for i in range(n):
        print(*res[i])
