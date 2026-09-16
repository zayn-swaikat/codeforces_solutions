lines = []
for i in range(5):
    line = input().split()
    lines.append([int(x) for x in line])

for i in range(5):
    for j in range(5):
        if lines[i][j] == 1:
            moves = abs(2-i) + abs(2-j)

print(moves)