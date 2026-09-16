line = input().split()
limak = int(line[0])
bob = int(line[1])

years = 0

while limak <= bob:
    limak *= 3
    bob *= 2
    years += 1

print(years)