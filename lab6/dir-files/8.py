import os

f = "A.txt"

l = r"C:\\Users\\isenb\\OneDrive\\Документы\\for school\\pp2\\lab6\\dir-files\\A.txt"

path = os.path.join(l,f)
os.remove(path)