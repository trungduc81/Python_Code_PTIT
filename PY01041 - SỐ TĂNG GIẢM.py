t = int(input())
for _ in range(t):
    s = input()
    i = 1
    if(len(s) < 3):
        print("NO")
        continue
    while i < len(s) and s[i] > s[i-1] : i += 1
    while  i < len(s) - 1 and s[i] > s[i+1] : i += 1
    if i==len(s) - 1:
        print("YES")
    else: print("NO")
