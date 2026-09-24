t = int(input())
for _ in range(t):

    n = int(input())
    s = input()

    max = 1
    counter = 1
    for i in range(n - 1):
        if s[i] == s[i+1]:
            counter += 1
        else:
            counter = 1
        if counter > max:
            max = counter

    print(max + 1)