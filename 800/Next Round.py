first_line = input()
all = int(first_line.split()[0])
k = int(first_line.split()[1])

grades = []
count = 0

line = input()
for j in range (len(line.split())):
    grades.append(int(line.split()[j]))

for i in range(len(grades)):
    if grades[i] >= grades[k-1] and grades[i] > 0:
        count += 1

print(count)