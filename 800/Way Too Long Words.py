number = int(input())
answers = []
for i in range(number):
    word = input()
    if len(word) > 10:
        new_word = word[0] + str(len(word) - 2) + word[len(word) - 1]
        answers.append(new_word)
    else:
        answers.append(word)
for item in answers:
    print(item)