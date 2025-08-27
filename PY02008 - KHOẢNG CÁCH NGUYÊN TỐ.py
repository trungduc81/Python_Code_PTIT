def sang():
    prime = [1] * (10**5)
    prime[0] = prime[1] = 0
    for i in range(2,int((10**5)**0.5)+1):
        if prime[i]:
            for j in range(i*i,(10**5),i):
                prime[j] = 0
    return [x for x in range(10**5) if prime[x]]

primes = sang()
n , x = map(int , input().split())
print(x,end = " ")
for i in range(n):
    x += primes[i]
    print(x,end = " ")
