m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

mark = [[0 for _ in range(n)] for _ in range(m)]
s = 0
for i in range(m):
    for j in range(n):
        if a[i][j] == -1:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n:
                        if mark[x][y] == 0 :
                            s += a[x][y]
                            mark[x][y] = 1
print(s)
