num = []
while len(num) < 10:
    num += list(map(int , input().split()))
se = set()
for i in range(10):
    se.add(num[i]%42)
print(len(se))
