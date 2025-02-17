def check(n):
    i=0
    while i<=n:
        yield i*i
        i+=1


n=int(input())
for j in check(n):
    print(j, end=" ")