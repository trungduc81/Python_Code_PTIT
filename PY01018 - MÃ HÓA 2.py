while True:
    line = input()
    if line =="0": break
    k , s = line.split()
    k = int(k)
    if k == 0: break
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    res = ""
    for i in range(len(s)):
        for j in range(len(P)):
            if s[i]==P[j]:
                ch = (j+k)%28
                res += P[ch]
                break
    res = res[::-1]
    print(res)
