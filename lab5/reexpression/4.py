import re

text = "Asojdfj, HDJLlsdjlsd, asjdfkAJDKHSOI"

pattern = r"\b[A-Z]{1}[a-z]+\b"

x = re.findall(pattern, text)

for i in x:
    print(i)