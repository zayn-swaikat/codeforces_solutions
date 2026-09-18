t = int(input())
result = []
for i in range(t):
    n = int(input())
    if n & (n-1) == 0 or n == 1:
        result.append("NO")
    else:
        result.append("YES")
print("\n".join(result))

"""

1 -> no   --> 1
2 -> no   --> 1 2
3 -> yes  --> 1 3
4 -> no   --> 1 2 4
5 -> yes  --> 1 5
6 -> yes  --> 1 2 3 6
7 -> yes  --> 1 7
8 -> no   --> 1 2 4 8
9 -> yes  --> 1 9
10 -> yes --> 1 2 5 10
11 -> yes --> 1 11
12 -> yes --> 1 2 3 4 6 12
14 -> yes --> 1 2 7 14
16 -> no  --> 1 2 4 8 16
32 -> no  --> 1 2 4 8 16 32

"""