n = int(input())
a = list()
for i in range(n):
    tmp = list(map(int , input().split()))
    a.append(tmp)
k = int(input())
sum1 , sum2 = 0 , 0
for i in range(n):
    for j in range(n):
        if j > i : sum1 += a[i][j]
        elif j < i : sum2 += a[i][j]
if abs(sum1-sum2) <= k:
    print("YES")
else: print("NO")
print(abs(sum1-sum2))
