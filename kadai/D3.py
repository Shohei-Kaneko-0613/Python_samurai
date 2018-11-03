class Shape():
    def __init__(self,s,reverse=False):
            self.s=s
            self.reverse=reverse
    
    def draw(self):
            if self.reverse:
                    for l1 in range(1,self.s+1):
                        for k1 in range(1,self.s+1):
                                if l1+k1 <= self.s+1:
                                        print("#",end="")
                        print()
        
            else:
                    for l2 in range(1,self.s+1):
                        for k2 in range(1,self.s+1):
                                if -4 <= l2-k2 <= 0:
                                        print("#",end="")
                                else:
                                        print(" ",end="")
                        print()        
    def area(self):
            print((self.s**2)/2)

a=True
b=False
shape1 = Shape(5,b)
shape1.draw()

