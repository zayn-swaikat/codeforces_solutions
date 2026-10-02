t = int(input())
for _ in range(t):

    m, n = map(int, input().split())
    grid = []

    for i in range(m):
        line = input()
        grid.append(line)

    # now i have to find the longest sequence of #
    maxi = 0
    b = 0
    for line in range(m):
        count = 0
        for i in range(n):
            if grid[line][i] == '#':
                count += 1
                if count > maxi:
                    maxi = count
                    b = i + 1
                    index = line + 1

    b -= maxi // 2.
    print(index, int(b))