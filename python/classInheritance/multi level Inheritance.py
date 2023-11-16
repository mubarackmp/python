class Animal:
    def speak(self):
        print("Animal speaking")

class Lion(Animal):
    def roar(self):
        print("Lion roaring")
        super().speak()


class Babylion(Lion):
    def eat(self):
        print("Baby Lion Eating meat")
        super().roar()
        

obj=Babylion()
obj.eat()