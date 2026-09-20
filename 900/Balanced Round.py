t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    line = list(map(int, input().split()))

    line.sort()

    maxi = 0
    counter = 0

    for i in range(n - 1):
        if line[i + 1] - line[i] <= k:
            counter += 1
        else:
            counter = 0

        if counter > maxi:
            maxi = counter

    answer = n - (maxi + 1)

    print(answer)




"""

8 3
17 3 1 20 12 5 17 12
1 3 5 12 12 17 17 20

1 3 5 xx xx xx xx xx
i should look for the bigger difference between two numbers
for example there:
the differences are: 

1 3 5 12 12 17 17 20
 2 2 7  0  5  0  3
bigger diffrence is obv 7



"""