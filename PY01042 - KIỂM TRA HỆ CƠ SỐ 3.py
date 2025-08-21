def check(s):
    for ch in s :
        if ch != '0' and ch != '1' and ch != '2':
            return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    if check(s): print("YES")
    else : print("NO")
