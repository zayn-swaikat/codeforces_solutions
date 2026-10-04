t = int(input())
for _ in range(t):
    n = int(input())
    line = list(map(int, input().split()))

    ans = line[-1] - line[0]

    for i in range(1, n):
        ans = max(ans, line[i] - line [0])

    for i in range(n - 1):
        ans  = max(ans, line[-1] - line[i])

    for i in range(n):
        ans = max(ans, line[i - 1] - line[i])


    print(ans)