line = input()
result = 'NO'
value = False
for char in line:
    # if char in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
    #     value = True
    #     x = int(char)
    # if char == '+' and value:
    #     x += 1
    #     break
    if char in ('H', 'Q', '9'):
        result = 'YES'
        break
print(result)