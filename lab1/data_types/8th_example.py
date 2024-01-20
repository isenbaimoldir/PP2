a = bytearray(3)
b = memoryview(a)
c = None

print(type(a), type(b), type(c))
print(a, b, c)
