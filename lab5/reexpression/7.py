import re

text = "my_variable, this_var_is_var"

x =''.join(x.capitalize() or '_' for x in text.split('_'))

print(x)