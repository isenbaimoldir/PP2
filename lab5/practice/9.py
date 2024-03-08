import re

f = open("row.txt", "r", encoding="utf8")
text = f.read()

ZNMPattern = r"\nЗНМ:\s*(?P<ZNM>\w{3}[0-9]{8})"
result = re.search(ZNMPattern, text)
if result:
    print(result['ZNM'])
else:
    print("NO")