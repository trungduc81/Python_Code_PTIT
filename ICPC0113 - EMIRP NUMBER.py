def sang():
    prime = [True] * (10**6+1)
    prime[0] = prime[1] = False
    for i in range(2, int((10**6)**0.5) + 1):
        if prime[i]:
            for j in range(i*i, 10**6+1, i):
                prime[j] = False
    return prime

def emrip(n):
    m = str(n)
    rev = m[::-1]
    return int(rev) != n and prime[int(rev)]

t = int(input())
prime = sang()
for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(2, n):
        if prime[i] and emrip(i):
            tmp = str(i)
            rev = tmp[::-1]
            if i < int(rev)  and int(rev) < n : print(i , rev , end = " ")
    print()
