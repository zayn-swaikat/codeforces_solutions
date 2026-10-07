# 598A

t = int(input())
for _ in range(t):

    n = int(input())
    sumi = n * (1 + n) // 2

    powers = (n).bit_length()
    sub = (2 ** powers - 1) * 2
    print(sumi - sub)