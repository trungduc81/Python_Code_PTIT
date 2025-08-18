s = input()
res = ""
cnt = 0
for i in s[::-1]:
    cnt += 1
    res += i
    if cnt== 3 :
        cnt = 0
        res += ","
if res[len(res)-1] == ',' :
    res = res[:-1]
    print(res[::-1])
else : print(res[::-1])
