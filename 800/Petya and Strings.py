first_string = input()
second_string = input()
first_string = first_string.lower()
second_string = second_string.lower()

result = "0"

for i in range(len(first_string)):
    if first_string[i] < second_string[i]:
        result = "-1"
        break
    if first_string[i] > second_string[i]:
        result = "1"
        break

print(result)