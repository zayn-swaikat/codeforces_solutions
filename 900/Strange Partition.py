import math

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    line = list(map(int, input().split()))

    mini = math.ceil(sum(line) / x)
    maxi = sum(math.ceil(i / x) for i in line)

    print(mini, maxi)

"""

175 69 757
153 72 735


"""