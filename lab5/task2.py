import re

a=input()
if re.search("a+b{2,3}$", a):
    print("Match")
else:
    print("Doesn`t match")