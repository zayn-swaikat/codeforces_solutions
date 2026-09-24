n, m = map(int, input().split())
days = 0
socks = n

while socks > 0:
    days += 1
    if days % m == 0:
        socks += 1
    socks -= 1

print(days)

"""

10 2
1 2 3 4 5 6 7 8 9 10
  11  12  13  14  15
      16      17
      18
      19

"""