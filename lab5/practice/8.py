import re

f = open("row.txt", "r", encoding="utf8")
text = f.read()

INK = r"\n.+\sОФД:\s+(?P<INK>[0-9]{6})"
result = re.search(INK, text)
if result:
    print(result['INK'])
else:
    print("No")