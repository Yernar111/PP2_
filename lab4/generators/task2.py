def check(n):
    i=2
    while i<n:
        yield i
        i+=2


n=int(input())
print(0, end="")
for j in check(n):
    print(",",j, end="")