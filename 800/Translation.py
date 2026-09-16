one = input()
two = input()
three = ''
for i in range(len(one) - 1, -1, -1):
    three += one[i]
if two == three:
    print('YES')
else:
    print('NO')