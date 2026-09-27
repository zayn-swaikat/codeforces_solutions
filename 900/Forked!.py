def solve():
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        xk, yk = map(int, input().split())
        xq, yq = map(int, input().split())

        directions = [(a, b), (a, -b), (-a, b), (-a, -b),
                    (b, a), (b, -a), (-b, a), (-b, -a),]

        kings = set()
        for dx, dy in directions:
            kings.add((xk + dx, yk + dy))

        queens = set()
        for dx, dy in directions:
            queens.add((xq + dx, yq + dy))

        answer = len(kings.intersection(queens))
        print(answer)

if __name__ == '__main__':
    solve()