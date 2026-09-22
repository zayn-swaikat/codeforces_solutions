t = int(input())
for _ in range(t):
    n = int(input())

    y = n % 2020
    x = (n - y*2021) // 2020

    if x >= 0:
        print("YES")
    else:
        print("NO")

"""

4041 yes
4042 yes

n = x*2020 + y*2020 + y
n = (x+y)*2020 + y


"""