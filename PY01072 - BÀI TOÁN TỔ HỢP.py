import itertools
n , k = map(int , input().split())
a = list(map(int , input().split()))
se = set(a)
a_sort = sorted(se)
for i in itertools.combinations(a_sort , k):
    print(*i)
