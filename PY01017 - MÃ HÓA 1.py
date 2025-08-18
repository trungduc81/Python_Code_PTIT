t = int(input())
while t>0:
    s = input()
    res= ""
    cnt = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]: cnt += 1
        else:
            res += str(cnt)
            res += s[i-1]
            cnt = 1
    res += str(cnt)
    res += s[len(s)-1]
    print(res)
    t -= 1
