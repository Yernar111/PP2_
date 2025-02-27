a=input("Enter a name of a text file: ")
b=input("Write an elements of list in 1 line: ").split()

c=open(a, "a")
for i in b:
    c.write(i+" ")
c.close()

d=open(a,"r")
print(d.read())
d.close
