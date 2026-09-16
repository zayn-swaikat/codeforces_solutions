first_line = input().split()
second_line = input().split()
friends = first_line[0]
fence = int(first_line[1])
width = 0
for person in second_line:
    if int(person) > fence:
        width += 2
    else:
        width += 1
print(width)