import math
def isprime(n):
    if n<2 : return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0 : return False
    return True

def check(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
        if (i%2 != 0 and int(s[i])%2 ==0) or (i%2 ==0 and int(s[i])%2 != 0):
            return False
    return isprime(sum)

t = int(input())
for _ in range(t):
    s = input()
    if check(s): print("YES")
    else : print("NO")
