for _ in range(int(input())):
    n = int(input())
    a = list(map(int , input().split()))
    b = list(map(int , input().split()))
    a.sort()
    b.sort()
    check = False
    for i in range(n):
        if a[i] > b[i] :
            check = True
            break
    if check: print("NO")
    else : print("YES")
