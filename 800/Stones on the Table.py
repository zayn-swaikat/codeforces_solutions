number = int(input())
row = input()
counter = 0
for i in range(len(row) - 1):

    if row[i] == row [i+1]:
        counter += 1

print(counter)