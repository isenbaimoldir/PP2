from math import factorial

def permutation(x):
    n = len(x)
    return factorial(n)

string = input()
print(permutation(string))