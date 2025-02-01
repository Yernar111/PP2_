def check1(a,b):
    return b//2-a

def check2(a,b):
    return 2*a-b//2

a=int(input())
b=int(input())
print("The amount of rabbits: ", check1(a,b))
print("The amount of chickens: ", check2(a,b))
