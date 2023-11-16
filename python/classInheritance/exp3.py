class car:
    def start_engine(self):
        print("engine started")
class electric_car(car):
    def start_engine(self):
        super().start_engine()
class gasoline_car(car):
    def start_engine(self):
       super().start_engine()  
obj1=electric_car()
obj2=gasoline_car()
obj1.start_engine()
obj2.start_engine()





        

