import re

a=input()
print(re.findall("[A_Z]{1}[a-z]+", a))