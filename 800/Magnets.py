number = int(input())
line = []
for i in range(number):
    magnet = input()
    line.append(magnet)

gaps = 0
for i in range(number - 1):
    if line[i] != line[i+1]:
        gaps += 1

print(gaps+1)