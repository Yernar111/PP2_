class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def show(self):
        print(self.x, self.y)
    
    def move(self):
        self.x=int(input("New coordinate of first point: "))
        self.y=int(input("New coordinate of second point: "))
        
    def dist(self):
        print(abs(self.x-self.y))
        

x=int(input())
y=int(input())
ab=point(x,y)
n=""
while n!="quit":
    n=str(input())
    if n=="show":
        ab.show()
    elif n=="move":
        ab.move()
    elif n=="dist":
        ab.dist()