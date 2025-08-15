t = int(input())
while t>0:
    n = int(input())
    check = 0
    while n > 0:
        m = n % 10
        if m != 4 and m != 7:
            check = 1
            break
        n //= 10
    if check == 0:
        print('YES')
    else:
        print('NO')
    t = t - 1
