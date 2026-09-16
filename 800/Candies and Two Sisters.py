"""

1 --> 0
2 --> 0
3 --> 1
4 --> 1
5 --> 2
6 --> 2
7 --> 3
8 --> 3
9 --> 4
10 --> 4

ok so as u notice theres a pair of each number
like for 1 and 2 the result is 0
     for 3 and 4 the result is 1
     for 5 and 6 the result is 2
and so on
ok but how do i know whats the result for a big number without having to count all the way from one up?
lets see:

1//2 = 0 --> 0
2//2 = 1 --> 0

3//2 = 1 --> 1
4//2 = 2 --> 1

5//2 = 2 --> 2
6//2 = 3 --> 2

so we notice:
if the number is even we divide it by 2 then print result - 1
if the number is  odd we divide it by 2 then print just the result

"""

t = int(input())
result = []
for i in range(t):
    number = int(input())
    if number % 2 == 0:
        result.append(number//2 - 1)
    else:
        result.append(number//2)
print("\n".join(str(i) for i in result))