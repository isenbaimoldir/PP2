def pal(x):
    n = len(x)
    for i in range(0, int(n/2)):
        if x[i] != x[len(x) - i - 1]:
            return "not a palindrome"
    return "yes, it's a palindrome"

word = input()
print(pal(word))