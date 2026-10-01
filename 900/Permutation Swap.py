import math

t = int(input())
for _ in range(t):

    n = int(input())
    line = list(map(int, input().split()))
    numbers = []
    for i in range(n):
        if line[i] != i + 1:
            numbers.append(abs(line[i] - 1 - i))

    print(math.gcd(*numbers))