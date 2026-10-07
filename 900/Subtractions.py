# 267A

t = int(input())
for _ in range(t):

    line = list(map(int, input().split()))
    line.sort()

    a = line[0]
    b = line[1]

    moves = 0

    while a > 0 and b > 0:

        line.sort()

        a = line[0]
        b = line[1]

        moves += b // a
        b %= a

        line = [a, b]

    print(moves)


"""

4 17
-----
4 13
4 9
4 5
4 1
-----
17 // 4 = 4
-----
3 1
2 1
1 1
1 0
-----
4 // 1 = 4

4 + 4 = 8

==========

18 21
-----

18 3
-----
21 // 18 = 1
-----
15 3
12 3
9 3
6 3
3 3
0 3


"""