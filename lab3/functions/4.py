def myfunction(a, b, /, *, c, d):
    print(a + b + c + d)

myfunction(1, 2, c = 3, d = 4)