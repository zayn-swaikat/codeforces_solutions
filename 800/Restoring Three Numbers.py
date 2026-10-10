# 1154A

line = list(map(int, input().split()))
line.sort()
one, two, three, four = line[0], line[1], line[2], line[3]
a = four - three
b = four - two
c = four - one
print(a, b, c)

"""

one = four - c
two = four - b
three = four - a
four = a + b + c

c = four - one
b = four - two
a = four - three


"""