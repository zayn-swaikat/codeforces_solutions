n = int(input())

superiors = []
for _ in range(n):
    superiors.append(int(input()))

maxi = 0
for i in range(n):
    depth = 1
    while superiors[i] != -1:
        i = superiors[i] - 1
        depth += 1
    maxi = max(depth, maxi)

print(maxi)