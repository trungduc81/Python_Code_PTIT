def sang(n):
    prime = [True] * (n+1)
    prime[0] = prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False
    return prime

t = int(input())
for _ in range(t):
    n = int(input())
    prime = sang(n)
    cnt = 0
    for i in range(2, n):
        if prime[i]:
            if i+6 < n and prime[i+2] and prime[i+6]:
                cnt += 1
            if i+6 < n and prime[i+4] and prime[i+6]:
                cnt += 1
    print(cnt)
