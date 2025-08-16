def solve(s):
    res = -10**18
    n = ""
    for i in range(len(s)):
        if(s[i].isdigit()) : n += s[i]
        else:
            if n != "":
                res = max(res, int(n))
                n = ""
    if n != "":
        res = max(res,int(n))
    return res

t = int(input())
while t>0:
    s = input()
    print(solve(s))
    t -= 1
