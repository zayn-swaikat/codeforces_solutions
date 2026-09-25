t = int(input())
for _ in range(t):
    a, b, n = map(int, input().split())
    line = list(map(int, input().split()))
    line.sort()

    counter = b

    for tool in line:
        counter += min(a - 1, tool)

    print(counter)