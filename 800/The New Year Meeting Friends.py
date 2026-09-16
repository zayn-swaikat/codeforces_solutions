line = list(map(int, input().split()))
line.sort()

a = line[0]
b = line[1]
c = line[2]

sum = b - a
sum += c - b

print(sum)

"""

1 4 7
1 + 4 + 7 = 12
12 / 3 = 4
1 -> 4 = 3
4 -> 4 = 0
7 -> 4 = 3
3 + 3 = 6

1 4 100
1 + 4 + 100 = 105
105 / 3 = 35
34 + 31 + 65 = 130

=====
WRONG
=====

lets pick the middle number 4
4-1 = 3
100 - 4 = 96
total = 99

ok lets pcik another set

1 2 100
2 - 1 = 1
100 - 2 = 98
total = 99

1 4 7
4 - 1 = 3
7 - 4 = 3
total = 6

10 10 100
10 - 10 = 0
100 - 10 = 90
total = 90


"""