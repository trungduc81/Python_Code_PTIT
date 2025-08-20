def reverse(n):
    sum = 0
    while n>0:
        sum = sum * 10 + n%10
        n //= 10
    return sum

t = int(input())
for _ in range(t):
    check = False
    cnt = 0
    n = int(input())
    while True:
        if cnt>1000: break
        if n%7==0:
            print(n)
            break
        else: cnt+=1
        rev = reverse(n)
        n = rev + n
    if cnt>1000:
        print("-1")
