t = int(input())
for _ in range(t):

    n, a, b = map(int, input().split())
    everything = "abcdefghijklmnopqrstuvwxyz"
    string = ""

    substring = everything[:b]

    for i in range(n):
        string += substring[i % b]

    print(string)

"""

lets take the eg 7 5 3:
the strings length is 7
every substring of length 5 should have exactly three distinct letters
so lets make the string "aeceeca"
so we can solve this by making the string consisting of only three letters
and repeat these letters
special cases:
if a =  1 and b = 1: all letters should be distinct
if a = n and b = 1: all letters should be the same
if a = 2 and b = 2: for each i letter the letter i+1 should be different

"""