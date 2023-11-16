# class 2


class Bank:
    def __init__(self,names,acnos,bals):
        self.names=names
        self.acnos=acnos
        self.bals=bals
   
    def deposit(self):
        amount=int(input("enter the amount""\n"))
        self.bals+=amount
    def withdraw(self):
        amount=int(input("enter the amount""\n"))
        self.bals-=amount
    def showaccdetails(self):
            print("name :",self.names)
            print(" account number :",self.acnos)
            print(" your balance is :",self.bals)      

l=[]
def createac():
    name=str(input("name""\n"))
    acno=int(input("accno""\n"))
    bal=int(input("balance""\n"))
    bank=Bank(name,acno,bal)
    l.append(bank)

while True:
    choice=int(input("1.create accounts inthe bank""\n""2.deposit""\n""3.withdraw""\n""4.show accounts details""\n""5.exit""\n""enter your choice: ""\n"))
    if choice==1:
        createac()
    elif choice==2:
        accountnumber=int(input("enter the account number-""\n"))
        for i in l:
            if accountnumber ==i.acnos:
                i.deposit()
                i.showaccdetails()
            
    elif choice==3:
        accountnumber=int(input("enter the account number-""\n"))
        for i in l:
            if accountnumber ==i.acnos:
                i.withdraw()
                i.showaccdetails()
    elif choice==4:
        for i in l:
            i.showaccdetails()
    elif choice==5:
        break
    else:
        print("wrong choice")
