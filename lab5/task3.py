import re

a=input()
print(re.findall("([a-z]+_[a-z]+)", a))