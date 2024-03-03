def to_zero(n):
    while n >= 0:
        x = n
        yield x
        n -= 1 

n = int(input())
for i in to_zero(n):
    print(i, end = " ")