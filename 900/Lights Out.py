grid = []
res = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
for _ in range(3):
    grid.append(list(map(int, input().split())))

for i in range(3):
    for j in range(3):
        if grid[i][j] % 2 == 1:
            res[i][j] ^= 1
            if i + 1 < 3: res[i + 1][j] ^= 1
            if i - 1 >= 0: res[i - 1][j] ^= 1
            if j + 1 < 3: res[i][j + 1] ^= 1
            if j - 1 >= 0: res[i][j - 1] ^= 1

for i in range(3):
    for j in range(3):
        print(res[i][j], end='')
    print()