# 313 B

string = input()
prefix = [0]
for i in range(len(string) - 1):
    if string[i] == string[i+1]:
        prefix.append(prefix[-1] + 1)
    else:
        prefix.append(prefix[-1])

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    res = prefix[r-1] - prefix[l-1]
    print(res)