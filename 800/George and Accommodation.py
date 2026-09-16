rooms = int(input())
counter = 0
for i in range(rooms):
    line = input().split()
    p = int(line[0])
    q = int(line[1])
    if q - p >= 2:
        counter += 1

print(counter)