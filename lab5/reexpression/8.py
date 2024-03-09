import re

text = "klsLSAJAklsa ffLKSskldfjklfassaA"

x = re.findall(r"[A-Z][^A-Z]*", text)

for i in x:
    print(x)