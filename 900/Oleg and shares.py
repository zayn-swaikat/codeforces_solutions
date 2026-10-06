# 793A

n, k = map(int, input().split())
line = list(map(int, input().split()))

mini = min(line)

ok = True
steps = 0

for item in line:
    if (item - mini) % k != 0:
        ok = False
        break

    steps += (item - mini) // k

print(steps if ok else '-1')

"""

mini  = item - nk
item - mini = nk
n = (item - mini) / k
if (item - mini) % k  != 0 etc

now we have to calculate n



"""