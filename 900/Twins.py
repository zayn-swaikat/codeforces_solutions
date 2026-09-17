n = int(input())
line = list(map(int, input().split()))
line.sort(reverse=True)
me = 0
him = sum(line)
i = 0
while him >= me:
    me += line[i]
    him -= line[i]
    i += 1
print(i)