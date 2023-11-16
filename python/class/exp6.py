# class 3

# Q4

class Time:
    def __init__(self,hours,minuts):
        self.h=hours
        self.m=minuts
    def addTime(self):
        c=int(input("enter the hour""\n"))
        d=int(input("enter the minute""\n"))
        self.h+=c
        self.m+=d
        if (self.m)>59:
            self.h+=1
            self.m-=60
            print("you first entered time is :",a,"hour",b,"minuts")
            print("you entered time is :",c,"hour",d,"minuts")
            print("added time is :",self.h,"hour",self.m,"minuts")
        else: 
            print("you first entered time is :",a,"hour",b,"minuts")
            print("you entered time is :",c,"hour",d,"minuts")
            print("added time is :",self.h,"hour",self.m,"minuts")
    def displayMinute(self):
        if self.h>0:
            self.m+=(self.h*60)
            print("totel minuts:",self.m)
        else:
            print("totel minuts:",self.m)
a=int(input("enter the hour""\n"))
b=int(input("enter the minute""\n"))
time=Time(a,b)
while True:
    choice=int(input("1.addTime""\n""2.displayMinute""\n""3.exit""\n""enter your choice""\n"))
    if choice ==1:
        time.addTime()
    elif choice ==2:
        time.displayMinute()
    elif choice==3:
        break
    else:
        print("wrong choice")




 