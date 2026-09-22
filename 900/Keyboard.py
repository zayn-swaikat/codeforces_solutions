direction = input()
string = input()
keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"

answer = ""

for item in string:
    i = keyboard.index(item)
    if direction == 'R':
        try:
            answer += keyboard[i-1]
        except:
            answer += ""
    else:
        try:
            answer += keyboard[i+1]
        except:
            answer += ""
print(answer)