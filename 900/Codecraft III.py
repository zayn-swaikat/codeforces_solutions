# 45A

months = {
    "January": 0,
    "February": 1,
    "March": 2,
    "April": 3,
    "May": 4,
    "June": 5,
    "July": 6,
    "August": 7,
    "September": 8,
    "October": 9,
    "November": 10,
    "December": 11
}

month = input()
k = int(input())
res = (months[month] + k) % 12

target = ""
for name, number in months.items():
    if number == res:
        target = name
        break

print(target)