t = int(input())
while t>0 :
    n = int(input())
    a = n%100
    while n >=100 : n //= 10
    if a==n: print("YES")
    else: print("NO")
    t -= 1
