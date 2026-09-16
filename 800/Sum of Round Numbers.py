import math

n = int(input())
final = []
for z in range(n):
    result = []
    numbers = []
    number = int(input())
    for i in range(len(str(number)) - 1, -1, -1):
        numbers.append(number)
        number %= int(math.pow(10, i))
    numbers.append(0)
    for i in range(len(numbers) - 1):
        if (numbers[i] - numbers[i+1]) != 0:
            result.append(numbers[i] - numbers[i+1])
    final.append([len(result), result])
for item in final:
    for x in item:
        if isinstance(x, list):
            print(" ".join(str(i) for i in x))
        else:
            print(x)

"""

9876 --> 9000
replaced digits from 1 to n with 0
new = old - replaced
876 --> 800

76 --> 70
6 --> 6

"""