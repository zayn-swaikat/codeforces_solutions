t = int(input())
for _ in range(t):
    n = int(input())
    line = list(map(int, input().split()))

    segments = 0
    if line[0] != 0:
        segments += 1
    for i in range(1, n):
        if line[i] != 0 and line[i - 1] == 0:
            segments += 1

    print(min(segments, 2))

"""

bc even whem we have segments>2:
we cal always choose the whole array
mak it all non zero
then change it back to zero
so the maximum is always 2


"""