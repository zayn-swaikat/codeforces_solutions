events = int(input())
line = input().split()
police = 0
counter = 0
for event in line:
    if event == '-1':
        if police > 0:
            police -= 1
        else:
            counter += 1
    else:
        police += int(event)
print(counter)