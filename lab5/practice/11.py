import re

f = open("row.txt", "r", encoding="utf8")
text = f.read()

pattern = r"\n(?P<order>[0-9]+)\."

#x = re.search(pattern, text)

result = re.finditer(pattern, text)

for x in result:
    print(x.group('order'))