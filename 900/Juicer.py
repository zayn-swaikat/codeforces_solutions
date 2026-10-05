# 709A

n, maxi, full = map(int, input().split())
oranges = list(map(int, input().split()))

size = 0
times = 0
for orange in oranges:
    if orange > maxi:
        continue
    size += orange
    if size > full:
        size = 0
        times += 1

print(times)