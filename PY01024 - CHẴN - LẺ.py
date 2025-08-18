def check(n):
    sum = 0
    while n>=10:
        a = n%10
        b = (n//10) % 10
        if abs(a-b) != 2: return False
        sum += a
        n //= 10
    sum += n
    if sum%10 != 0 : return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    if check(n): print("YES")
    else : print("NO")
