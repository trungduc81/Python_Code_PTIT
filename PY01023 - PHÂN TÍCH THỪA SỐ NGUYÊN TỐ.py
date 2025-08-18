t = int(input())
for _ in range(t):
    n = int(input())
    print("1",end = " ")
    i = 2
    cnt = 0
    while i*i <= n:
        while n%i ==0:
            cnt += 1
            n //= i
        if cnt > 0:
            print("* " + str(i) + "^" + str(cnt),end = " ")
            cnt = 0
        i+=1
    if n > 1 : print("* " + str(n)+"^1",end = " ")
    print()

