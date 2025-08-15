s = input()
cnt1 = cnt2 = 0
for i in s:
    if i.islower():
        cnt1 += 1
    else:
        cnt2 += 1
if cnt1 >= cnt2 :
    print(s.lower())
else:
    print(s.upper())
