from collections import Counter

t = int(input())
for _ in range(t):

    n = int(input())
    units = list(map(int, input().split()))

    triads = [units[x] + units[x + 2] - units[x + 4] for x in range(n - 4)]

    cnt = Counter(triads)
    res = 0
    for item in cnt.values():
        res += item * (item - 1) // 2

    for i in range(n - 4):
        if i + 2 < n - 4 and triads[i] == triads[i+2]:
            res -= 1
        if i + 4 < n - 4 and triads[i] == triads[i+4]:
            res -= 1

    print(res)