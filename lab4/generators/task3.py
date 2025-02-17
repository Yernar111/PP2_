def check(n):
    i=0
    while i<=n:
        yield i
        i+=12


n=int(input())
for j in check(n):
    print(j, end=" ")