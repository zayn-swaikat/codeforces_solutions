stops = int(input())
people_stop = []
people = 0
for i in range(stops):
    line = input().split()
    exit = int(line[0])
    enter = int(line[1])
    people -= exit
    people += enter
    people_stop.append(people)
print(max(people_stop))