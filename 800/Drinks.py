number = int(input())
line = input().split()
result = 0
for i in range(number):
    result += int(line[i])
print(result/number)