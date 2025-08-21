from collections import deque

a = ['0' , '2' , '4' , '6' ,'8']
def solve(n):
    dq = deque(['2', '4', '6', '8'])
    while dq:
        tmp = dq.popleft()
        pld = int(tmp + tmp[::-1])
        if pld < n and len(str(pld)) % 2 == 0:
            print(pld,end = " ")
        if len(tmp) < len(str(n))/2 :
            for i in a:
                dq.append(tmp + i)
    print()

t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)



