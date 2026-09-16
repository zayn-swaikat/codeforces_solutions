number = int(input())
final = []
for i in range(number):
    line = list(map(int, input().split()))
    a = line[0]
    b = line[1]
    c = line[2]
    if (a + b == c) or (a + c == b) or (c + b == a):
        final.append("YES")
    else:
        final.append("NO")
for item in final:
    print(f"{item}")