t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())

    if 2*b - c > 0 and (2*b - c) % a == 0:
        print("YES")
    elif (a + c) / 2 > 0 and ((a + c) / 2) % b == 0:
        print("YES")
    elif 2*b - a > 0 and (2*b - a) % c == 0:
        print("YES")
    else:
        print("NO")


"""

10 5 30
ok so lets see
they should be in a decreasing or increasing order
options are:

10 5 30
↘ ↗ have to change middle
a + 2d = c
d = (c - a) / 2


10 20 15
↗ ↘ have to change last

20 10 0
↘ ↘ any

↗ ↗ any

i cant make a number less than its original value

1.
b - m*a = c - b
m*a = 2*b - c
m = (2*b - c) / a > 0

2.
b*m - a = c - b*m
2bm = c + a
m = (c + a / 2b) > 0

3.
mc - b = b - a
mc = 2b - a
m = (2b - a) / c > 0


"""