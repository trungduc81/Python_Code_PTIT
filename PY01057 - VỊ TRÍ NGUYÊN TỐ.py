import math
def isprime(n):
    if n<2 : return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

a = ['2','3','5','7']
t = int(input())
for _ in range(t):
    s = input()
    i = 0
    while i < len(s):
        if (isprime(i) and s[i] in a) or (not isprime(i) and s[i] not in a): i += 1
        else:
            break
    if i == len(s) :
        print("YES")
    else:
        print("NO")
