tests = int(input())
result = []
for i in range(tests):
    length = int(input())
    line = input()
    first = line.find("B")
    edited = line[::-1]
    last = length - (edited.find("B"))
    result.append(last - first)
print("\n".join(str(i) for i in result))