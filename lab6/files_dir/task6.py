a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b=".txt"
for i in range(26):
    c=a[i]+b
    d=open(c, "w")

d.close()