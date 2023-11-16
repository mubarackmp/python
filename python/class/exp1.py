# class 

class Bank:
    def __init__(self,name,acno,bal):
        self.name=name
        self.acno=acno
        self.bal=bal

    def deposit(self):
        amount=int(input("enter the amount""\n"))
        self.bal+=amount
        print("your balance is",self.bal)
    def withdraw(self):
        amount=int(input("enter the amount""\n"))
        self.bal-=amount
        print("your balance is",self.bal)
name=str(input("enter your name Sir""\n"))
acno=int(input("enter your account number Sir""\n"))
bal=int(input("enter the amount""\n"))
bank=Bank(name,acno,bal)
# bank.deposit()
bank.withdraw()