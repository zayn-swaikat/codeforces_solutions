one = input()
two = input()
new = ''
for i in range(len(one)):
    if one[i] != two[i]:
        new += '1'
    else:
        new += '0'
print(new)