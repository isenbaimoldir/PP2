def filter_prime(x):
    num = 0
    if x < 2:
        return False
    for i in range(2, int(x) + 1):
        if x % i == 0:
            num += 1
    if num > 1:
        return False
    return True

numbers = list(map(int, input().split()))
for i in numbers:
    if filter_prime(i):
        print(i)
    else:
        pass