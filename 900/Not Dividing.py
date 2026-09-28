t = int(input())
for _ in range(t):

    n = int(input())
    line = list(map(int, input().split()))

    done = False

    while not done:
        done = True
        for i in range(n - 1):
            if line[i+1] % line[i] == 0:
                if line[i] == 1:
                    line[i] += 1
                else:
                    line[i + 1] += 1
                done = False

    print(*line)