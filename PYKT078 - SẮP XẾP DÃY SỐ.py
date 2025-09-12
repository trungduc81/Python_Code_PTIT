for _ in range(int(input())):
    n , m = map(int , input().split())
    a = list(map(int , input().split()))
    tmp = []
    for i in range(n):
        if i == a.index(max(a)):
            tmp.append(m)
        tmp.append(a[i])
    print(*[int(x) for x in tmp if x < 0],end = " ")
    print(*[int(x) for x in tmp if x >= 0])


