line = input().split()
price = int(line[0])
money = int(line[1])
bananas = int(line[2])

total = 0

for i in range(bananas):
    total += (i + 1)*price

if total > money:
    print(total - money)
else:
    print("0")