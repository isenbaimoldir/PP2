def reverse(x):
    words = x.split() 
    rev = ""
    for i in words:
        rev = i + " " + rev
    return rev.strip()

s = input()
print(reverse(s))