k = int(input())
line = list(map(int, input().split()))

line.sort(reverse=True)
counter = 0
length = 0

for i in range(12):
    if length < k:
        length += line[i]
        counter += 1
    if length >= k:
        break

if length >= k:
    print(counter)
else:
    print(-1)