t = int(input())
result = []

for i in range(t):
    number = int(input())
    # isVanya = True
    # vanya = False
    # for i in range(10):
    #     if number+1 % 3 == 0:
    #         number += 1
    #     elif number-1 % 3 == 0:
    #         number -= 1
    #     else:
    #         number += 1
    #     if isVanya and number % 3 == 0:
    #         result.append("FIRST")
    #         vanya = True
    #         break
    #     isVanya *= False
    # if not vanya:
    #     result.append("SECOND")
    if number % 3 == 0:
        result.append("Second")
    else:
        result.append("First")
print("\n".join(result))


"""

10 % 3 = 1 --> vanya
11 % 3 = 2 --> vanya
12 % 3 = 0 - 11 - 12
13 % 3 = 1 --> vanya

"""