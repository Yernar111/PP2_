import re

a=input()
x=re.sub("[ ,.]", ":", a)
print(x)