# class 3

# Q2

while True:
    choice=int(input("1.Celcius to farenheit calculator""\n""2.Farenheit to Celcius calculator""\n""3.exit""\n""enter your choice""\n"))
    if choice ==1:
        class Temperature:
            def __init__(self,celcius):
                self.celc=celcius
            def convertFarenheit(self):
                a=((self.celc)*(9/5))+32
                print("ferenheit :",a)
            

        cel=int(input("enter the Celcius you want to convert""\n"))
        temperature1=Temperature(cel)
        temperature1.convertFarenheit()
    elif choice ==2:
        class Temperature:
            def __init__(self,farenheit):
                self.far=farenheit
            def convertCelcius(self):
                c=((self.far)-32)*(5/9)
                print("Celcius:",c)

        faren=int(input("enter the Farenheit you want to convert""\n"))
        temperature1=Temperature(faren)
        temperature1.convertCelcius()
    elif choice==3:
        break
    else:
        print("wrong choice")