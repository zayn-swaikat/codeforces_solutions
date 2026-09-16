line = input().split()
number = int(line[0])
times = int(line[1])
for i in range(times):
    if str(number)[len(str(number)) - 1] == '0':
        number = number // 10
    else:
        number -= 1
print(number)