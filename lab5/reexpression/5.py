import re

text = "aksjdfkjb, aekjacv jldksjfl aslkjles aksjdlvb aLKJSDLF aKJSDJOFJb"

pattern = r"a\w+b\b"

x = re.findall(pattern, text)

for i in x:
    print(i)