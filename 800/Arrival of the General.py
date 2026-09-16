import math

number = int(input())
line = list(map(int, input().split()))

high = max(line)
maxi = line.index(high)

if maxi == 0:
    steps = 0
else:
    steps = maxi

line.insert(0, high)
line.pop(maxi+1)

low = min(line)
lowi = -1

for i in range(number):
    if line[i] == low:
        lowi = i

if lowi == number - 1:
    steps += 0

steps += (number - lowi - 1)

print(steps)

line.insert(number, low)
line.pop(lowi)