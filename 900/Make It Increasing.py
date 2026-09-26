t = int(input())
for _ in range(t):

    n = int(input())
    line = list(map(int, input().split()))

    counter = 0
    possible = True

    for i in range(n - 2, -1, -1):
        while line[i] >= line[i + 1] and line [i] > 0:
            line[i] //= 2
            counter += 1

        if line[i] >= line[i + 1]:
            possible = False
            break

    if possible:
        print(counter)
    else:
        print(-1)