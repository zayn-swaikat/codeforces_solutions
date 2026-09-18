n = int(input())
columns = list(map(int, input().split()))
columns.sort()
print(" ".join(map(str, columns)))

"""

3 2 1 2

"""