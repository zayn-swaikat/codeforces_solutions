t = int(input())
for _ in range(t):

    n, k = map(int, input().split())

    if n % 2 == 0:
        if k % 4 == 0:
            print(n)
        elif k % 4 == 1:
            print(n - k)
        elif k % 4 == 2:
            print(n + 1)
        else:
            print(n + k + 1)

    else:
        if k % 4 == 0:
            print(n)
        elif k % 4 == 1:
            print(n + k)
        elif k % 4 == 2:
            print(n - 1)
        else:
            print(n - k - 1)

"""

0 1:
-1

0 2:
-1 + 2 = 1

0 3:
-1 +2 -3 = -2

10 10:
10 -1 +2 +3 -4 -5 +6 +7 -8 -9 +10 = 11

10 11:
10 -1 +2 +3 -4 -5 +6 +7 -8 -9 +10 +11 = 22

11 10:
11 +1 -2 -3 +4 +5 -6 -7 +8 +9 -10 = 10

11 11:
11 +1 -2 -3 +4 +5 -6 -7 +8 +9 -10 -11 = -1

ok so so as we can see:
when we start with an even number like 10:
we subtract 1 then add 2, add 3 subtract 4 subtract 5 etc

when we start with an odd number like 11:
add 1 subtract 2 subtract 3 add 4 add 5 etc

is there any way i can make an equation out of this?
lets see

when we start with even:

first i always add the real number
so we have n
n -1 +2 +3 -4 -5 ... t
(-1 +2 +3 -4 -5 ... t) this has to make a rule

if t is even:
-1 -4 -5 -8 -9 -12 -13
+2 +3 +6 +7 +10 +11 +14
=======================
1

if t is odd:
-1 -4 -5 -8 -9 -12 -13
+2 +3 +6 +7 +10 +11
=======================
-13 which is -t

ok so
if n is even and t is even:
n + 1

if n is even and t is odd:
n - t

ok no this doesnt work on all numbers

hmmmm

lets focus on k:

if n is even:
n = 10
k = 8 % 4 = 0
k = 9 % 4 = 1
k = 10 % 4 = 2
k = 11 % 4 = 3

10 8
10
n
-----
10 9
1
n - k
-----
10 10
11
n + 1
-----
10 11
22
n + k + 1

==========

11 8
11
n
-----
11 9
20
n + k
-----
11 10
10
n - 1
-----
11 11
-1
n - k - 1

"""