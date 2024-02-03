def function(x):
    return lambda a: a * x

mydoubler = function(2)
print(mydoubler(11))
