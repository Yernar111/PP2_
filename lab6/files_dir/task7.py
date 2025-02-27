a=input("Name of a file you want to copy: ")
b=input("Name of a file you want to paste: ")
c=open(a, "r")
d=open(b, "w")
d.write(c.read())

c.close()
d.close()