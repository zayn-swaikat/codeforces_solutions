line = list(map(int, input().split()))
n = line[0]
m = line[1]
for i in range(n):
    if i % 2 == 0:
        print("#" * m)
    elif (i+3)%4 == 0:
        print("." * (m-1) + "#")
    else:
        print("#"+ "." * (m-1))



'''

#########   i = 0
........# i = 1
######### i = 2
#........
######### i = 4
........# i = 5
######### i = 6
#........
######### i = 8


'''