n, m = map(int, input().split())
moves = min(n, m)
if moves % 2 == 0:
    print("Malvika")
else:
    print("Akshat")
# while n*m != 0:
#     n -= 1
#     m -= 1
#     aks = not aks
# if aks:
#     print("Akshat")
# else:
#     print("Malvika")


"""

1 1 --> 1 --> aks
1 2 --> 2 --> aks
1 3 --> 3 --> aks
2 2 --> 4 --> mal
5 1 --> 5 --> aks
2 3 --> 6 --> mal
3 3 --> 9 --> aks
5 2 --> 10 --> mal
                    1 11 -> 11 --> aks
3 4 --> 12 --> aks
7 2 --> 14 --> mal
4 4 --> 16 --> mal
25 70 --> 1750 --> aks

each time someone chooses n -= 1, m-= 1

"""