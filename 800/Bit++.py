number = int(input())
x=0
for i in range(number):
    statement = input()
    if (statement == "X++") or (statement == "x++") or (statement == "++X") or (statement == "++x"):
        x += 1
    elif (statement == "X--") or (statement == "x--") or (statement == "--X") or (statement == "--x"):
        x -= 1
    else:
        print("Invalid statement")
print(x)