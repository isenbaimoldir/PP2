import re

strings = ['a', 'ab', 'abb', 'abbb', 'ac', 'bc', 'bac', 'bbb']

pattern = r'^a[b]*$'

for string in strings:
    result = re.search(pattern, string)
    if result:
        print(string)
    else:
        print("NO")
