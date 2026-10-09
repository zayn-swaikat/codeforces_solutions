# 1337B

t = int(input())
for _ in range(t):
    h, n, m = map(int, input().split())

    while n > 0 and 10 < h - h // 2:
        h //= 2
        h += 10
        n -= 1

    if m * 10 >= h:
        print("YES")
    else:
        print("NO")


"""

h // 2 + 10 < h
10 < h - h // 2


"""