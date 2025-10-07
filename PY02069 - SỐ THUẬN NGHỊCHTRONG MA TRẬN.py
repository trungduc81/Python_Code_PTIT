def pld(x):
    s = str(x)
    return len(s) >=2 and s == s[::-1]
n , m = map(int , input().split())
a = []
for i in range(n):
    arr = list(map(int , input().split()))
    a.append(arr)
MAX = -1
pos = []
for i in range(n):
    for j in range(m):
        tmp = a[i][j]
        if(pld(tmp)):
            if tmp > MAX :
                MAX = tmp
                pos = [(i,j)]
            elif tmp == MAX :
                pos.append((i,j))
if MAX == - 1 : print('NOT FOUND')
else :
    print(MAX)
    for i , j in pos :
        print(f"Vi tri [{i}][{j}]")

