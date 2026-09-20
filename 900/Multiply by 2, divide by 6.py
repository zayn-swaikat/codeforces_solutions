t = int(input())
for i in range(t):
    n = int(input())
    counter = 0
    twos = 0
    threes = 0
    x = n
    ok = True

    while x % 2 == 0:
        x = x // 2
        twos += 1

    while x % 3 == 0:
        x = x // 3
        threes += 1

    if twos > threes:
        ok = False
        counter = -1

    if x != 1:
        ok = False
        counter = -1

    if ok:
        counter = 2*threes - twos
    print(counter)


"""

1       (0)
3 + 3   (2)
6 + 3   (1)
9 + 9   (4)
18 + 18 (3)
36 + 18 (2)
54 + 27 (5)
81      (8)

3 ** 0
3 * 1
3 * 2
3 * 3
3 * 6
3 * 12
3 * 18
3 * 27
3 * 36
3 * 45


12 = 2^2 * 3
18 = 2 * 3^2


"""