n = int(input())
line = input().lower()
full = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
f = set(full)
if n < 26 :
    print("NO")
else:
    ugh = set(" ".join(line).split())
    if ugh == f:
        print("YES")
    else:
        print("NO")