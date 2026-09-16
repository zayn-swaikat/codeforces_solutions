money = int(input())

hundred = money // 100
remain = money % 100

twenty = remain // 20
remain %= 20

ten = remain // 10
remain %= 10

five = remain // 5
one = remain % 5

print(hundred + twenty + ten + five + one)