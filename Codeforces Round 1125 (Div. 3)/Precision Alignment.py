def is_free(a, b, c):
    return a > b or a > c or b > c

def cost(a, b, c, S):
    s = a + b + c

    if S <= s:
        return 0

    if is_free(a, b, c):
        return S - s

    if a == b == c:
        return None

    L = min(b - a, c - b) + 1
    return (S - s) + 2 * L

n, k = map(int, input().split())
labs = []
for _ in range(n):
    a, b, c = map(int, input().split())
    labs.append((a, b, c))

for a, b, c in labs:
    s = a + b +c
    