import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    letters = 'abcdefghijklmnopqrstuvwxyz'
    times = [0] * 26
    res = []

    for i in range(n):
        for j in range(26):
            if times[j] == array[i]:
                res.append(letters[j])
                times[j] += 1
                break

    print(''.join(res))