import re

text = input()

x =''.join(x.capitalize() or '_' for x in text.split('_'))

print(x)