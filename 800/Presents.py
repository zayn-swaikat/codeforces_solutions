number = int(input())
line = input().split()

result = ['0'] * number
for i in range(number):
    result[int(line[i]) - 1] = str(i+1)

print(' '.join(result))