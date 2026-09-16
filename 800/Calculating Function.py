number = int(input())
if number % 2 == 0:
    print(number//2)
else:
    result = -1 * ((number+1) // 2)
    print(result)