while True:
    n = int(input())
    se = set()
    if n==0: break
    if n==1:
        print(1)
    else:
        while n>1:
            se.add(n)
            if n%2==0 : n//=2
            else: n = n*3 +1
        print(len(se)+1)


