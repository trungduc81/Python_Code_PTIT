n = int(input())
A = list(map(int, input().split()))
st = list()
for x in A:
    if st and (st[-1] + x) % 2 == 0:
        st.pop()
    else:
        st.append(x)
print(len(st))
