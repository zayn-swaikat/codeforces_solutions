first_line = input().split()
students = int(first_line[0])
time = int(first_line[1])
line = input()
result = list(line)
final = ''

for j in range(time):
    i = 0
    while i < (students - 1):
        if (result[i] == 'B' and result[i+1] == 'G'):
            result[i] = 'G'
            result[i+1] = 'B'
            i += 2
        else:
            i+= 1

for item in result:
    final += item

print(final)