def cv(s):
    n = ""
    for i in range(len(s)):
        if i%2 != 0:
            for j in range(int(s[i])):
                n += s[i-1]
    return n

t = int(input())
while t>0:
    s = input()
    print(cv(s))
    t -= 1
