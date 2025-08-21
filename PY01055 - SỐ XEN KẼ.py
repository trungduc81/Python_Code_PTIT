def check(s):
    if len(s)%2 == 0 or s[0] == s[1] : return False
    for i in range(0,len(s),2):
        if s[i] != s[0]: return False
    return True

t = int(input())
for _ in range(t):
    n = input()
    if check(n):print("YES")
    else : print("NO")
