line = list(map(int, input().split()))

a = line[0]
b = line[1]
c = line[2]

sum = 0
distance = 0

for item in line:
    sum += item
point = sum // 3

distance += abs(a - point)
distance += abs(b - point)
distance += abs(c - point)

print(distance)

"""

1 4 7
1 + 4 + 7 = 12
12 / 3 = 4
1 -> 4 = 3
4 -> 4 = 0
7 -> 4 = 3
3 + 3 = 6

"""