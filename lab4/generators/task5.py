def check(a):
    i=a
    while i>=0:
        yield i
        i-=1


a=int(input())
for j in check(a):
    print(j, end=" ")