def palindrome(s):
    x = ''.join(reversed(s))
    if s == x:
        print("the string is palindrome")
    else:
        print("string is not palindrome")

string = input()
palindrome(string)