t = int(input())
for _ in range(t):

    n = int(input())
    line = input().strip()

    stack = []
    res = []
    for i, command in enumerate(line, 1):
        if command == '1':
            stack.append(i)
        elif command == '2':
            if stack:
                stack.pop()
                res.append(i)
    res.extend(stack)
    res.sort()
    print(len(res))
    print(*res)