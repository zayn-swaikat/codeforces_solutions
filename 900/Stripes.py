t = int(input())
for _ in range(t):
    input()
    grid = [input() for _ in range(8)]

    if 'RRRRRRRR' in grid:
        print('R')
    else:
        print('B')