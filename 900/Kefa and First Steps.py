"""

n = int(input())
line = list(map(int, input().split()))
final = []

for i in range(1, n+1):

    previous = line[:i]
    final.append(previous)

print(final)

for i in range(n):
    new = final[i]
    for j in range(len(new) - 3):
        if new[j] > new[j+1]:
            new = new[j+1:]
    print(new)

2 2 1 3 4 1
1 2 1 2 3 1

2 2 9
1 2 3



"""

n = int(input())
line = list(map(int, input().split()))
counter = 1
result = 1

for i in range(1, n):
    if line[i] >= line[i-1]:
        counter += 1
        if counter > result:
            result = counter
    else:
        counter = 1

print(result)