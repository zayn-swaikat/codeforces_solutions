t = int(input())

for _ in range(t):
    wheels = int(input())

    if wheels % 2 == 1 or wheels < 4:
        print(-1)
        continue

    mini = (wheels + 5) // 6
    maxi = wheels // 4

    print(mini, maxi)


"""

minimum number of busses is that all busses have 6 tires
maximum number of busses is that all busses have 4 tires

    minim    maxim
4     1        1
26    5        6

alright so as we can see:
wheels / 6 = 26 / 6 = 4.sth
so ceil(wheels/6) = 5 = minimum

maximum = wheels // 4 = 26 // 4 = 6

"""