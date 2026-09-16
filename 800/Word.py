word = input()
lower = 0
upper = 0
for letter in word:
    if letter.upper() == letter:
        upper += 1
    else:
        lower += 1

result = ""
if upper > lower:
    for letter in word:
        result += letter.upper()
else:
    for letter in word:
        result += letter.lower()

print(result)