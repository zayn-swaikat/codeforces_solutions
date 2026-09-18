n, m = map(int, input().split())
line = list(map(int, input().split()))
line.sort()
mini = max(line) - min(line)
for i in range(m - n + 1):
    if line[i + n - 1] - line[i] < mini:
        mini = line[i + n - 1] - line[i]
print(mini)