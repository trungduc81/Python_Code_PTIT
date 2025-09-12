n = int(input())
a = []
for i in range(n):
    tmp = list(input().strip())
    a.append(tmp)
sum = 0
for i in range(n):
    cnt = 0
    for j in range (n):
        if a[i][j] == 'C': cnt += 1
    sum += cnt*(cnt-1)//2
for j in range(n):
    cnt = 0
    for i in range(n):
        if a[i][j] == 'C' : cnt += 1
    sum += cnt*(cnt-1)//2
print(sum)


