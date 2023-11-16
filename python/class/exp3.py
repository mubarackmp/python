# class 3

# Q1

class Circle:
    def __init__(self,radius):
        self.area=radius
    def getArea(self):
        a=((3.14)*((self.area)**2))
        print("area of circle:",a)
    def getCircumstances(self):
        c=((2)*(3.14)*(self.area))
        print("circumstance of circle:",c)
area=int(input("enter the area of your circle""\n"))
circle=Circle(area)
while True:
    choice=int(input("1.getArea""\n""2.getCircumstance""\n""3.exit""\n""enter your choice""\n"))
    if choice ==1:
        circle.getArea()
    elif choice ==2:
        circle.getCircumstances()
    elif choice==3:
        break
    else:
        print("wrong choice")