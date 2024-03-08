import re

f = open("row.txt", "r", encoding="utf8")
text = f.read()

BINpattern = r"\nБИН\s+(?P<BIN>[0-9]{12})"

print(re.search(BINpattern, text).group('BIN'))