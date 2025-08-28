from collections import Counter
import math
def isprime(n):
    if n < 2:return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True
n = int(input())
a = list(map(int, input().split()))
cnt = Counter(a)
for key, value in cnt.items():
    if isprime(key):
        print(key, value)
