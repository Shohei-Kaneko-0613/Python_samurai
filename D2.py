class Shape:
    def __init__(self,s):
        self.s=s
    def draw(self):
        
        for i in range(1,self.s+1):
            for j in range(1,self.s+1):
                if i+j <= self.s+1:
                    print("#",end="")
            print()
    def area(self):
        print((self.s**2)/2)

Shape1 = Shape(5)
Shape1.draw()
Shape1.area()
