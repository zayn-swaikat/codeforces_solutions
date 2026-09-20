n, m = map(int, input().split())
line = list(map(int, input().split()))
line.sort()

result = 0

for item in line[:m]:
    if item < 0:
        result -= item

print(result)