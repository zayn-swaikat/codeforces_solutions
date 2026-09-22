def is_palindrome(word):
    ok = True
    for i in range(len(word)):
        if word[i] != word[len(word) - i - 1]:
            ok = False
    return ok

n, k = map(int, input().split())
word = input()




"""

when can i call a word a palindrome?
when its flipped version is the same word
like lol
alright so in this problem we should delete k letter from the word
then decide if the rest can form a palindrome
hmmm so lets see
after deleting
if the word has even number of letters
each letter must be repeated even number of times
if the word has odd numbr of letters
then each letter must be repeated even number of times too
but one of the letters must be repeated odd number of times4


"""