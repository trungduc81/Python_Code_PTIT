import math
def isprime(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i ==0 : return False
    return True
t = int(input())
for _ in range(t):
    s = input()
    if len(s) < 4:
        print("NO")
        continue
    if isprime(int(s[-4:])):
        print("YES")
    else: print("NO")

