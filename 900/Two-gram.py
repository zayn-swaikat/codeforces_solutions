n = int(input())
word = input()
two_grams = []
for i in range(n - 1):
    two_grams.append(word[i] + word[i+1])

try:
    result = max(two_grams, key=two_grams.count)
except:
    result = word
print(result)