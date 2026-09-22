t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    array = list(map(int, input().split()))
    prefix = [0]
    for num in array:
        prefix.append(prefix[-1] + num)
    total = sum(array)
    for i in range(q):
        start, end, value = map(int, input().split())
        temp = total
        part_sum = prefix[end] - prefix[start - 1]
        temp -= part_sum
        temp += (end - start + 1) * value
        if temp % 2 == 0:
            print("NO")
        else:
            print("YES")




"""

2 2 1 3 2
2 3 4

2 4 4 3 2


"""