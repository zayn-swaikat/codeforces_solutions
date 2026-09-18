word = list(input())
i = 0
while i < len(word) - 2:
    if word[i] + word[i + 1] + word[i + 2] == "WUB":
        word.pop(i + 2)
        word.pop(i + 1)
        word.pop(i)
        if word[i-1] != " ":
            word.insert(i, " ")
        i = 0
    else:
        i += 1
print(("".join(word)).strip())

"""
          or
=======================
word.replace("WUB", "")

"""