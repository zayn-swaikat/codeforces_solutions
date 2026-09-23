t = int(input())
for _ in range(t):
    s = input()
    zeros = 0
    ones = 0
    for num in s:
        if num == '0':
            zeros += 1
        else:
            ones += 1
    mini = min(zeros, ones)
    if mini % 2 == 0:
        print("NET")
    else:
        print("DA")

# s = input()
# alica = True
# while 


"""

01 odd odd : da
1111 even even : net
0011 even even : net

01 alica
1111 bob
0011 bob
011 alica


"""