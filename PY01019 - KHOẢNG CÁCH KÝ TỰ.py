import math
t = int(input())
while t > 0:
    s = input()
    rev = s[::-1]
    check = 0
    for i in range(1, len(s)):
        kc1 = ord(s[i]) - ord(s[i-1])
        kc2 = ord(rev[i]) - ord(rev[i-1])
        if abs(kc1) != abs(kc2):
            check = 1
            break
    if check == 0:
        print("YES")
    else:
        print("NO")
    t -= 1
