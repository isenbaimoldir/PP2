import functools

l = [1,2,3,4,5]
print(reduce(lambda x, y: x * y, l))