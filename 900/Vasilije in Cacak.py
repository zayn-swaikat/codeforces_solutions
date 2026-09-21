t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    mini = 0
    maxi = 0
    ok = True
    i = 0
    while i < k:
        maxi += n-i
        i += 1
    j = 1
    while j <= k:
        mini += j
        j += 1
    if x < mini or x > maxi:
        ok = False
    if ok:
        print("YES")
    else:
        print("NO")