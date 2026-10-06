# 1582 B

t = int(input())
for _ in range(t):

    n = int(input())
    array = list(map(int, input().split()))

    ones = array.count(1)
    zeros = array.count(0)

    res = ones * (2 ** zeros)
    print(int(res))