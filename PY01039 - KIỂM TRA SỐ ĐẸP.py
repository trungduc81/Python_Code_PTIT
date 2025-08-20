def check(n):
    for i in range(len(n)-2):
        if n[i] == n[i+1]: return False
        if n[i] != n[i+2]: return False
    return True

t = int(input())
for _ in range(t):
    n = input()
    if check(n):
        print("YES")
    else: print("NO")
