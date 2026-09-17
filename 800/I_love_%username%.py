n = int(input())
line = list(map(int, input().split()))
counter = 0
for i in range(1, n):
    previous = line[:i]
    if all(line[i] > j for j in previous):
        counter += 1
    if all(line[i] < j for j in previous):
        counter += 1
print(counter)