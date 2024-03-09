import re

text = "klsLSAJAklsa ffLKSskldfjklfassaA"

x = re.sub(r'(?<=\w)([A-Z])', r' \1' ,text)

print(x)