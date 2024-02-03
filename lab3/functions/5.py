def myfunction(x):
    if(x > 0):
        return x + myfunction(x - 1)
    else:
        return 0
print(myfunction(5))