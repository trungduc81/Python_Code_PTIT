def check(s):
    return s[0] == s[len(s)-1]

t = int(input())
for _ in range(t):
    n = input()
    if check(n): print("YES")
    else : print("NO")
