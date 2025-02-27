a=input("Enter a name of a text file: ")
b=open(a, "r")
n=0
for i in b:
    n+=1

print(f"The number of lines in a file: {n}")
b.close()