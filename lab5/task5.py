import re

a=input()
if re.search("a.+b$", a):
    print("Match")
else:
    print("Doesn`t match")