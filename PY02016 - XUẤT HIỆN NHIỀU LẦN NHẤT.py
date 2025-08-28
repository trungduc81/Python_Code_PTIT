from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int , input().split()))
    cnt = Counter(a)
    most = cnt.most_common(1)[0] #most_common([1]) tra ve 1 list cac tuple
    if most[1] > n/2 : print(most[0])
    else : print("NO")

