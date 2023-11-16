
class Animal:
    def speak(self):
        print("Animal speaking")

class dog(Animal):
    def boww(self):
        super().speak()
        print("dog boww")
class cat(Animal):
    def meawwu(self):
        print("cat meawwu ")
class cow(Animal):
    def goww(self):
        print("cow goww")

obj1=cow()
obj2=cat() 
obj3=dog() 
obj2.meawwu()
obj3.boww()
obj1.goww()       






