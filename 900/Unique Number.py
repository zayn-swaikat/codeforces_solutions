t = int(input())
for _ in range(t):

    n = int(input())
    if n > 45:
        print(-1)
        continue
    res = []
    i = 9
    while i > 0:
        take = min(i, n)
        res.append(take)
        n -= take
        i -= 1
    print(int(''.join(map(str, res[::-1]))))