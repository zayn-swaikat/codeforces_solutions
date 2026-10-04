t = int(input())
for _ in range(t):

    n = int(input())
    string = input()
    ans = string.count('map')
    string = string.replace('map', '*')
    ans += string.count('pie')
    print(ans)