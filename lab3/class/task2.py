class shape:
    a=0
    def area(self):
        print(self.a*self.a)

class square(shape):
    def __init__(self, length):
        self.a=length

a=square(int(input()))
a.area()
