x = input()
up, low = 0, 0

for i in x:
    if i.isupper():
        up += 1
    else:
        low += 1
print(up, low)