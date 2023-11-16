# class employee:
#     def __init__(self,salary):
#         self.s=salary

#     def calculate_salary(self):
#         ta=900
#         da=1000
#         days=int(input("enetr the days you worked""\n"))
#         bonus=days*250
#         self.s=ta+da+bonus
# class Manager(employee):
#     def salary(self):
#         basic_salary=int(input("enter the basic salary of manager:""\n"))
#         super().calculate_salary()
#         self.s=self.s+basic_salary
#         print("your total salary: ",self.s)

# class Developer(employee):
#     def salary(self):
#         basic_salary=int(input("enter the basic salary of Developer:""\n"))
#         super().calculate_salary()
#         self.s=self.s+basic_salary
#         print("your total salary: ",self.s)
# while True:
#     choice=int(input("1.Salary of manager""\n""2.Salary of Developer""\n""3.exit""\n""enter your choice""\n"))
#     if choice ==1:
#         obj=Manager(0)
#         obj.salary()
#     elif choice ==2:
#         ob=Developer(0)
#         ob.salary()
        
#     elif choice==3:
#         break
#     else:
#         print("wrong choice")



class bank_account:
    def __init__(self,deposit,withdraw):
        self.d=deposit
        self.w=withdraw
    def account_details(self,name,accountno,deposit,withdraw,balance):
        self.name=name
        self.accountno=accountno
        self.deposit=deposit
        self.withdraw=withdraw  
        self.balance=balance  
class savingsaccount(bank_account): 
    def





















