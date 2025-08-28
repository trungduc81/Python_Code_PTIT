n = int(input())
a = list(map(float , input().split()))
cnt ,sum ,  MAX , MIN = 0 ,0 ,  max(a) , min(a)
for i in range(n):
    if a[i] != MAX and a[i] != MIN:
        sum += a[i]
        cnt += 1
res = sum / cnt
print("%.2f" % res)


