import re

txt = "LATE__klsad, asldf_sjlke, OAHD_LDKJFL, jklsjfd_kaskj, lsjdfkj"

pattern = r"[a-z]+_[a-z]+"

x = re.findall(pattern, txt)

for i in x:
    print(i)