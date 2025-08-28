from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    a = list()
    for i in range(n):
        x = int(input())
        a.append(x)
    cnt = Counter(a)
    MAX = max(cnt.values())
    res = [key for key,value in cnt.items() if value == MAX ]
    print(min(res))
