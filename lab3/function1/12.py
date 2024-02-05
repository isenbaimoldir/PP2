def histogram(x):
    for i in range(x):
        print("*", end='')

nums = list(map(int, input().split()))
for i in nums:
    histogram(i)
    print()