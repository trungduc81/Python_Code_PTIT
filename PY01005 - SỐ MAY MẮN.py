n = int(input())
cnt = 0
while n>0:
    m = n%10
    if m==4 or m ==7 :
        cnt += 1
    n//=10
if cnt==4 or cnt==7:
    print('YES')
else:
    print('NO')
