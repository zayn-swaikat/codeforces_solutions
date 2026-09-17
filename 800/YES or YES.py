t = int(input())
result = []
for i in range(t):
    word = input()
    if word.upper() == "YES":
        result.append("YES")
    else:
        result.append("NO")
print("\n".join(result))