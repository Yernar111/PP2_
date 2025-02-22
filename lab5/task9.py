import re

a=input()
x=re.sub(".(?=[A-Z])"," ", a)
print(x)