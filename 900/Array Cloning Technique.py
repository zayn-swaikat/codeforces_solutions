t = int(input())
for _ in range(t):
    n = int(input())
    line = list(map(int, input().split()))
    line.sort()

    most_repeated = 1
    run = 1
    for i in range(1, n):
        if line[i] == line[i - 1]:
            run += 1
        else:
            run = 1
        most_repeated = max(most_repeated, run)

    if most_repeated == n:
        print(0)
        continue

    clones = 0
    moves = n - most_repeated
    while most_repeated < n:
        clones += 1
        most_repeated *= 2

    print(clones + moves)


"""

0 1 3 3 7 0

0 0 1 3 3 7
0 0 1 3 3 7

0 0 0 0 3 7
0 0 0 0 3 7

0 0 0 0 0 0
===============

   4 3 2 1
1- 4 3 2 1
2- 4 4 2 1
3- 4 4 2 1
4- 4 4 4 1
5- 4 4 4 4

ok so as we can see first we decide which element is gonna be cloned
and that element is the most repeated one
lets name the times it appeared in the list n
1- clone
2-n : swap n times
n+1 : clone again
n+2: swap min(2n, array - new n)

"""