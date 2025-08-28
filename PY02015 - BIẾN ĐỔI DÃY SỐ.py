while True:
    a = list(map(int, input().split()))
    if a == [0, 0, 0, 0]: break
    cnt = 0
    while True:
        if a[0] == a[1] == a[2] == a[3]: break
        tmp = [abs(a[i] - a[i+1]) for i in range(3)]
        tmp.append(abs(a[3] - a[0]))
        a = tmp
        cnt += 1
    print(cnt)
