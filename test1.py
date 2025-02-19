import re

x=open("lorem", "r")
#y="abcd efgh"
#print(re.search("^abcd", y))
for i in x:
    i=i.rstrip()
    print(re.search("Lorem", i))
