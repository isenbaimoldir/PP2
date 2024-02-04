def prime(x):
    if x < 2:
        return False
    num = 0
    for i in range(2, int(x) + 1):
        if x % i == 0:
            num += 1
    if num > 2:
        return False
    return True

numbers = list(map(int, input().split()))

print(list(filter(lambda x: prime(x), numbers)))
