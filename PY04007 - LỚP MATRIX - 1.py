for _ in range(int(input())):
    n , m = map(int , input().split())
    a = []
    for i in range(n):
        tmp = list(map(int , input().split()))
        a.append(tmp)
    rev = list(map(list,zip(*a))) #zip(*matrix) de chuyen ma tran thanh chuyen vi
    res = []
    for _ in range(n):
        res.append([0]*n)
    for i in range(n):
        for j in range(n):
            for k in range(m):
                res[i][j] += a[i][k] * rev[k][j]
    for i in range(n):
        print(*res[i])



