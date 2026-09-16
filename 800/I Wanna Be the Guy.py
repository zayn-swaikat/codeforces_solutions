levels = int(input())
x = input().split()
y = input().split()

x.pop(0)
y.pop(0)

all = set([])
for i in range(1, levels + 1):
    all.add(str(i))

final = set(x + y)

if '0' in final:
    final.remove('0')

if all == final:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")