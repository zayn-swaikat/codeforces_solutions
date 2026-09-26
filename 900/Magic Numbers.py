n = input()
n = n.replace('144', 'x')
n = n.replace('14', 'x')
n = n.replace('1', 'x')
n = n.replace('x', '')

if n == '':
    print("YES")
else:
    print("NO")