def square(a, b):
    for i in range(a, b+1):
        if i**2 > b:
            break
        else:
            yield i**2

a = int(input())
b = int(input())

for i in square(a,b):
    print(i)