import re
def check(a):
    b=""
    for i in range(1,len(a)):
        if a[i-1]==" ":
            b+=a[i].lower()
        else:
            b+=a[i]
    return b

a=input()
a=check(a)
x=re.sub(" ", "_", a)
print(x)