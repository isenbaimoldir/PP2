thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#shortest
[print(x) for x in thislist]