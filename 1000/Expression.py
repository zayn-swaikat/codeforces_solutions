a = int(input())
b = int(input())
c = int(input())

one = a + b + c
two = a * b + c
three = a + b * c
four = a * b * c
five = (a + b) * c
six = a * (b + c)

print(max(one, two, three, four, five, six))

"""

257 71 766
271 73 780

"""