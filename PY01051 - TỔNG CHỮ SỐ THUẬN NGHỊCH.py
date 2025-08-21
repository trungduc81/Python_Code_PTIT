def pld(s):
    if len(s) < 2 : return False
    return s == s[::-1]
t = int(input())
for _ in range(t):
    n = int(input())
    sum = 0
    while n>0:
        sum += n%10
        n //= 10
    if pld(str(sum)):print("YES")
    else : print("NO")

