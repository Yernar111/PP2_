class shape:
    a=0
    def area(self):
        print(self.a*self.a)

class rectangle(shape):
    def __init__(self, length, width):
        self.a=length
        self.b=width
    def area(self):
        print(self.a*self.b)

a=rectangle(int(input()), int(input()))
a.area()
