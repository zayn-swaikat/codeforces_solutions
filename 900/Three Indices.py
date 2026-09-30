t = int(input())
for _ in range(t):

    n = int(input())
    line = list(map(int, input().split()))

    ok = False
    for i in range(1, n - 1):
        a = next((j for j in range(i) if line[i] > line[j]), None)
        b = next((j for j in range(i+1, n) if line[i] > line[j]), None)

        if a is not None and b is not None:
            ok = True
            print("YES")
            print(a+1, i+1, b+1)
            break

    if not ok:
        print("NO")