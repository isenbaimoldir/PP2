thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)