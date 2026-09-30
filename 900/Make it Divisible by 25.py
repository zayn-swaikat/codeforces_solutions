def check(n, target):
    j = n.rfind(target[1])
    if j == -1:
        return None
    i = n.rfind(target[0], 0, j)
    if i == -1:
        return None
    return (len(n) - 1 - j) + (j - i - 1)


t = int(input())

for _ in range(t):
    n = input().strip()
    answers = []

    for target in ["00", "25", "50", "75"]:
        result = check(n, target)
        if result is not None:
            answers.append(result)

    print(min(answers))



"""

i should look for the closest '00' or '50' or '25' or '75'

1176587


"""