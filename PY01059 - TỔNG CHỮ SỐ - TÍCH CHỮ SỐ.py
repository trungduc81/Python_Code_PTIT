def ktra(s):
    for i in range(1,len(s),2):
        if s[i] != '0' : return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    sum , res = 0 , 1
    for i in range(len(s)):
        if i%2==0: sum += int(s[i])
        else :
            if s[i] != '0' : res *= int(s[i])
    print(sum,end = " ")
    if ktra(s): print("0")
    else : print(res)


