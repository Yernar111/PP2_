def check(a,b):
    i=a
    while i<=b:
        yield i*i
        i+=1


a=int(input())
b=int(input())
for j in check(a,b):
    print(j, end=" ")