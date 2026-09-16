number = int(input())
result = ""

for i in range(number):
    if i == 0:
        result += "I hate"
    elif i % 2 == 1:
        result += " that I love"
    else:
        result += " that I hate"

print(result, "it")