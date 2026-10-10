# 1676A

t = int(input())
for _ in range(t):

    ticket = input()
    first = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    second = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    if first == second:
        print("YES")
    else:
        print("NO")