t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    mini = k * (1 + k) // 2
    maxi = k * (2*n - k +1) // 2
    ok = True
    if x < mini or x > maxi:
        ok = False
    if ok:
        print("YES")
    else:
        print("NO")