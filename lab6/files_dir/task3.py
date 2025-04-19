import os

a=input("Name of a file you want to delete: ")
b=os.access(a, os.F_OK)
if b:
    os.remove(a)
else:
    print("File does not exist")