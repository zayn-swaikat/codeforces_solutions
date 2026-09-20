n = int(input())
if n >= 0:
    answer = n
else:
    if n >= -10:
        answer = 0
    else:
        number = str(n*-1)
        length = len(number)
        if (number[length - 1]) >= (number[length - 2]):
            answer = -1 * (int(number) // 10)
        else:
            answer = -1 * (int(number[:length-2] + number[length-1]))
print(answer)

"""

-15
-15 // 10 = -1
-15 + 10 = -5

-147 + 


"""