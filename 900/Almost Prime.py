def is_prime(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def almost_prime(n):
    count = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            if is_prime(i):
                count += 1
    if count == 2:
        return True
    else:
        return False

n = int(input()) + 1
counter = 0
for i in range(1, n):
    if almost_prime(i):
        counter += 1

print(counter)