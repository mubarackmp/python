import math
class Shape:
    def __init__(self,area):
        self.a=area
    def area(self):
        print("area of the shape :",self.a)
class Circle(Shape):
    def area1(self):
        r=int(input("enter the radius""\n"))
        self.a=(math.pi)*((r)**2)
        super().area()
class Rectangle(Shape):
    def area2(self):
        l=int(input("enter the length""\n"))
        b=int(input("enter the breadth""\n"))
        self.a=l*b
        super().area()
while True:
    choice=int(input("1.Circle""\n""2.Rectangle""\n""3.exit""\n""enter your choice""\n"))
    if choice ==1:
        obj=Circle(0)
        obj.area1()
    elif choice ==2:
        ob=Rectangle(0)
        ob.area2()
        
    elif choice==3:
        break
    else:
        print("wrong choice")