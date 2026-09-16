problems = int(input())
done = 0
for i in range(problems):
    count = 0
    solution = input()
    for j in solution:
        if j=='1':
            count += 1
    if count > 1:
        done += 1
print(done)