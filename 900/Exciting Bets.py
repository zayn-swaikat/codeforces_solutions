t = int(input())
for _ in range(t):

    a, b = map(int, input().split())

    if a == b:
        print("0 0")
        continue

    gcd = abs(a - b)

    moves = min(a % gcd, gcd - (a % gcd))

    print(gcd, moves)