line = list(map(int, input().split()))
n = line[0]
k = line[1]

if n % 2 == 0:
    if k <= n/2:
        print(k * 2 - 1)
    else:
        print((k - n//2) * 2)
else:
    if k <= (n//2 + 1):
        print(k*2 - 1)
    else:
        print(2*(k - n//2 - 1))



"""

MEMORY LIMIT EXCEEDED
=====================

then im missing sth out:
lets see
its always gonna be:
1 3 5 7 9 ..... 2 4 6 8 10 ...
so its def up to the number k
if n is even: then len evens = len odds
if n is odd: then len odds = len evens + 1
lets take an e.g:

10:

1 3 5 7 9 2 4 6 8 10

10 1
1
10 2
3
10 3
5
10 4
7
10 5
9

15:

1 3 5 7 9 11 13 15 2 4 6 8 10 12 14

15 1
1
15 7
13
15 8
15

ok so if the number is even, like 10:
then theres 5 odds and 5 evens

so like if k <= n/2 then the number is odd
otherwise its gonna be even
but how do we know which number its gonna be?
or like which even or odd number its gonna be?
ok so if we know its odd:
then k < n/2:
and lets take the e.g 10 4
k = 4 < 10 / 2 = 5
so final = 7 = 4 * 2 = 8 - 1
10 3
3 * 2 - 1 = 6 - 1 = 5
10 2
2 * 2 - 1 = 4 - 1 - 3
10 5
5 * 2 - 1 = 9
ok yepppiiiii its workinnnn :D
alright ill write it down then move to the even numbers
done

10 6
(6 - 10/2) * 2 = 2
10 7
(7 - 10/2) * 2 = 4
10 8
(8 - 10/2) * 2 = 6
yepppiii omg its workingggggggg


if n is odd like 11
1 3 5 7 9 11 2 4 6 8 10

if k is 6
then its k <= n//2 + 1
and result = k * 2 - 1
else
if k is 7
result = 2(k - n//2 - 1))
2(7 - 5 - 1) = 2
if k is 8
2(8 - 5 - 1) = 4
if k is 9
2(9 - 5 - 1) = 6

"""