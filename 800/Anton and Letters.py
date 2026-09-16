letters = input()
if letters == '{}':
    print(0)
else:
    letters = letters.split(', ')
    letters[0] = list(' '.join(letters[0])).pop(2)
    letters[len(letters) - 1] = list(' '.join(letters[len(letters) - 1])).pop(0)
    print(len(set(letters)))