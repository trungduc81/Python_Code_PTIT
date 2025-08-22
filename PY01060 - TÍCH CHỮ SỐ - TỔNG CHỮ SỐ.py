
t = int(input())
for _ in range(t):
    s = input()
    sum , res = 0 , 1
    for i in range(len(s)):
        if i%2==1: sum += int(s[i])
        else :
            if s[i] != '0' : res *= int(s[i])
    print(res , sum)


