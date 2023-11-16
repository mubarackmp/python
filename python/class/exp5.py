# class 3

# Q3

class Students:
    def __init__(self,name,rollnum,age,mark):
        self.names=name
        self.rollnum=rollnum
        self.age=age
        self.mark=mark
    def showstudentsdetails(self):
        print("name :",self.names,"\n")
        print("roll number is :",self.rollnum,"\n")
        print(" age is :",self.age,"\n")
        print(" mark is :",self.mark,"\n""\n")
    def setAge(self):
        ages=int(input("enter the age""\n"))
        self.age=ages
    def setMark(self):
        marks=int(input("enter the mark""\n"))
        self.mark=marks

l=[]
def createid():
    name=str(input("name""\n"))
    roll=int(input("rollno""\n"))
    age=0
    mark=0
    students=Students(name,roll,age,mark)
    l.append(students)

while True:
    choice=int(input("1.create students  id""\n""2.setAge""\n""3.setMarks""\n""4.show students details""\n""5.exit""\n""enter your choice: ""\n"))
    if choice==1:
        createid()
    elif choice==2:
        rollnumber=int(input("enter the Roll number-""\n"))
        for i in l:
            if rollnumber ==i.rollnum:
                i.setAge()
                i.showstudentsdetails()
            
    elif choice==3:
        rollnumber=int(input("enter the Roll number-""\n"))
        for i in l:
            if rollnumber ==i.rollnum:
                i.setMark()
                i.showstudentsdetails()
    elif choice==4:
        for i in l:
            i.showstudentsdetails()
    elif choice==5:
        break
    else:
        print("wrong choice")