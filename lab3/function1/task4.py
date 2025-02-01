def check(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

a=input().split()
b=[0]*len(a)
for i in range(len(a)): b[i]=int(a[i])
c=list(filter(check,b))
print(c)