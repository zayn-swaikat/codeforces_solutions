t = int(input())
for _ in range(t):

    a, b, c, d = map(int, input().split())
    if (d > a and d < b) and not (c > a and c < b):
        print("YES")
        continue

    if (d > b and d < a) and not (c > b and c < a):
        print("YES")
        continue

    if (c > a and c < b) and not (d > a and d < b):
        print("YES")
        continue

    if (c > b and c < a) and not (d > b and d < a):
        print("YES")
        continue

    print("NO")

"""

hmm i had an idea that in order to them to intersect the difference between a,b or c,d should be at least two. 
this way theres at least a number between them
then the second must is that c (or d) should be between a and b
while the other one should be also between but from the other side

so lets take an example
a = 2, b = 9, c = 10, d = 6
we can notice how d:6 is a < d < b
and how c:10 doesnt follow a < c < b
alright so thats the rule


"""