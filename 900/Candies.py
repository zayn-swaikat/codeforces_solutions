t = int(input())
for _ in range(t):
    n = int(input())
    found = False

    k = 2
    while not found:
        if n % (2**k - 1) == 0:
            found = True
            print(n // (2**k - 1))
        k += 1


"""

x + 2x + 4x + 8x + 16x
1 + 2 + 4 + 8 + 16
2 + 4 + 8 + 16 + 32
3 + 6 + 12 + 24

n = 28 --> 

x + 2x + 4x + 8x + 2^k-1 x = n
x(1 + 2 + 4 + 8 + 2^k-1)
x = n / (1 + 2 + ... + 2^k-1)

1+2+4+⋯+2^k−1
k = 1 -> 1
k = 2 -> 3
k = 3 -> 7
k = 4 -> 15

كل مرة عم ضيف 2^k-1

x = n / (1 + 2 + ... + 2^k-1)
x = n / (2^k - 1)


"""