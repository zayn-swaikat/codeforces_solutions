import math

n = int(input())
result = []
for i in range(n):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    counter = 0
    if a <= b:
        counter = b - a
    else:
        counter = math.ceil(a/b) * b - a
    result.append(str(counter))
print('\n'.join(result))

"""
its always gonna be a number between 0 and b

12 5
2.4
3*5 - 12

15 6
2.5
3*6 - 15

126 10
12.6
13*10 - 126

good job ziki :3

"""