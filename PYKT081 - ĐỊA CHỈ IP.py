def check(a):
    if len(a) != 4 : return False
    for i in range(len(a)):
        if not a[i].isdigit(): return False
        if not (0 <= int(a[i]) <= 255) : return False
    return True
for _ in range(int(input())):
    tmp = input().split(".")
    if  check(tmp):
        print("YES")
    else : print("NO")
