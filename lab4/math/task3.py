import math
n=int(input("Input number of sides: "))
a=int(input("Input the length of a side: "))
b=a/(2*math.tan(math.pi/n))
s=0.5*(n*a)*b
print(f"The area of the polygon is: {s}")