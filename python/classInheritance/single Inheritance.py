class Animal:
    def speak(self):
        print("Animal speaking")

class Lion(Animal):
    def roar(self):
        print("Lion roaring")
obj=Lion()
obj.roar()
obj.speak()