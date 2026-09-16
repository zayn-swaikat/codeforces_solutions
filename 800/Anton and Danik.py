number = int(input())
line = input()
danik = anton = 0
for letter in line:
    if letter == 'A':
        anton += 1
    if letter == 'D':
        danik += 1
if anton > danik:
    print("Anton")
elif anton < danik:
    print("Danik")
else:
    print('Friendship')