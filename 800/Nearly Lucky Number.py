number = input()
lucky = 0
yes = 'YES'
for digit in number:
    if digit == '4' or digit == '7':
        lucky += 1
for digit in str(lucky):
    if (digit not in ('4', '7')):
        yes = 'NO'
print(yes)