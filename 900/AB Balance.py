# t = int(input())
# for _ in range(t):

#     string = input()
#     ab = 0
#     ba = 0

#     for i in range(len(string) - 1):
#         if string[i] == 'a' and string[i + 1] == 'b':
#             ab += 1
#         elif string[i] == 'b' and string[i + 1] == 'a':
#             ba += 1

#     if ab == ba:
#         print(string)
#         continue

#     elif ba > ab:
#         also = ba - ab
#         i = 0
#         while i < len(string) - 1 and also > 0:
#             if string[i] == 'b' and string[i + 1] == 'a':
#                 string = string[:i] + 'a' + string[i + 1:]
#                 also -= 1
#             i += 1

#     else:
#         also = ab - ba
#         i = 0
#         while i < len(string) - 1 and also > 0:
#             if string[i] == 'a' and string[i + 1] == 'b':
#                 string = string[:i] + 'b' + string[i + 1:]
#                 also -= 1
#             i += 1
#     print(string)

t = int(input())

for _ in range(t):
    s = input()

    if s[0] != s[-1]:
        s = ('b' if s[0] == 'a' else 'a') + s[1:]

    print(s)