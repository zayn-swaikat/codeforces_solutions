t = int(input())
for _ in range(t):

    n = int(input())

    answer = 1
    while n % answer == 0:
        answer += 1

    print(answer - 1)


"""

20

25


"""