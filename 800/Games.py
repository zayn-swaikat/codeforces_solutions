"""

    home   guest
1.    1      2
2.    2      4
3.    3      4

1 - 2 :
1 : 4 - 2 : 2

1 - 3 :
1 : 4 - 2 : 3

2 - 3 :
2 : 4 - 4 : 3

     home    guest
1.    100      42
2.     42     100
3.     5       42
4.    100      5

1 - 2 :
100 : 100 - 42 : 42

1 - 3 :
100 : 42 - 42 : 5

1 - 4 :
100 : 5 - 42 : 100

2 - 3 :
42 : 42 - 100 : 5

2 - 4 :
42 : 5 - 100 : 100

3 - 4 :
5 : 5 - 42 : 100


alright so i can see that when

"""

t = int(input())
teams = []
matches = []
count = 0

for i in range(t):
    line = input().split()
    home = line[0]
    guest = line[1]
    team = [home, guest]
    teams.append(team)

for i in range(len(teams)):
    for j in range(len(teams)):
        if i != j:
            matches.append([teams[i], teams[j]])

for match in matches:
    a = match[0]
    b = match[1]
    if a[1] == b[0]:
        count += 1

print(count)