def kgiam(n):
    while n>=10:
        a = n%10
        b = (n//10)%10
        if a<b: return False
        n //= 10
    return True
t = int(input())
while t>0:
    n = int(input())
    if not kgiam(n):
        print("NO")
    else: print("YES")
    t -= 1
