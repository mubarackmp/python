class calculation1:
    def addition(self,x,y):
        return x+y
class calculation2:
    def multiplication(self,x,y):
        return x*y
class derived(calculation1,calculation2):
    def divition(self,a,b):
        return a//b
    
obj=derived()
print(obj.addition(4,2))
print(obj.multiplication(4,2))
print(obj.divition(4,2))