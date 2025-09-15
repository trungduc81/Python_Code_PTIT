def cv(score):
    if 3 <= score <= 4 :
        return 2.5
    elif 5 <= score <= 6 :
        return 3.0
    elif 7 <= score <= 9:
        return 3.5
    elif 10 <= score <= 12:
        return 4.0
    elif 13 <= score <= 15:
        return 4.5
    elif 16 <= score <= 19:
        return 5.0
    elif 20 <= score <= 22:
        return 5.5
    elif 23 <= score <= 26:
        return 6.0
    elif 27 <= score <= 29:
        return 6.5
    elif 30 <= score <= 32:
        return 7.0
    elif 33 <= score <= 34:
        return 7.5
    elif 35 <= score <= 36:
        return 8.0
    elif 37 <= score <= 38:
        return 8.5
    elif 39 <= score <= 40:
        return 9.0

for _ in range(int(input())):
    a = input().split()
    lis , read  = cv(int(a[0])) , cv(int(a[1]))
    tmp = (lis + read + float(a[2]) + float(a[3])) / 4
    temp = int(tmp)
    if tmp - temp >= 0.75 :
        print(temp + 1.0)
    elif tmp -temp >= 0.25:
        print(temp + 0.5)
    else : print(float(temp))

