import re

text = "lkjs, oisjo. sdlfkj. ldhfl,"
pattern = r"[ ,.]"

x = re.sub(pattern, ':', text)
print(x)
