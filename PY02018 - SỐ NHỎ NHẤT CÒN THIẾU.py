n = int(input())
a = list(map(int , input().split()))
tmp = 0
while True:
    tmp+=1
    if tmp not in a:
        print(tmp)
        break
