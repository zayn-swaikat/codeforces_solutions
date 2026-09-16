def function(year):
    distinct = False
    if len(set(str(year))) == len(str(year)):
        distinct = True
    return distinct

year = int(input())
found = False
while not found:
    year += 1
    if function(year):
        found = True
        print(year)