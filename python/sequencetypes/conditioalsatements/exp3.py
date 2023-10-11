# ---------> question 1 <-----------

# a=int(input("enter a number"))
# if(a%7==0):
#     print("numer is divisible by 7")
# else:
#     print("number is not divisible")


# ---------> question 2 <-----------

# a=int(input("enter a number"))
# if(a%5==0):
#     print("hello")
# else:
#     print("bye")



# ---------> question 3 <-----------


# a=int(input("enter a number"))
# b=a%10
# print(b)



# ---------> question 4 <-----------


# a=int(input("enter a number"))
# b=a%10
# if(b%3==0):
#     print("last number is divisible by 3")
# else:
#     print("last number is not divisible")



# ---------> question 5 <-----------

# a=int(input("enter consumed unit"))
# if(a>100 and a<200):
#     b=(a-100)*5
#     print("totel bill is",b)
# elif(a>200):
#     b=(a-200)*10+500
#     print("totel bill is",b)
# else:
#     print("no charge")


# ---------> question 6 <-----------

# a=int(input("enter a number between 1-7""\n"))
# b=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
# if(a>0 and a<8):
#  print(b[a-1])
# else:
#  print("number is not in the range")
  
 

# ---------> question 7 <-----------

# a=int(input("enter a number between 1-12""\n"))
# b=["January","February","March","April","May","June","July","August","September","October","November","December"]
# if(a>0 and a<8):
#     if(a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12):
#         print("31 Days")
#         print(b[a-1])
#     elif(a==4 or a==6 or a==9 or a==11):
#         print("30 Days")
#         print(b[a-1])
#     else:
#         print("28 or 29 Days")
#         print(b[a-1])
# else:
#     print("number is not in the range")


# ---------> question 8 <-----------

# a=int(input("enter number of days""\n"))
# if(a==30):
#     print("April,June,September,November")
# elif(a==31):
#     print("January,March,May,July,August,October,December")
# elif(a==28 or a==29):
#     print("February")
# else:
#     print("there is no months wth this number of dates")


# ---------> question 9 <-----------

# a=int(input("enter your age""\n"))
# if(a>=18):
#     print("you are eligble for voting")
# else:
#     print("you are not eligible for voting")


# ---------> question 10 Q6<-----------

# a=int(input("enter length of first side of triangle""\n"))
# b=int(input("enter length of second side of triangle""\n"))
# c=int(input("enter length of third side of triangle""\n"))
# if(a==b and a==c):
#     print("triangle is equilateral")
# elif(a!=b and a!=c and b!=c):
#     print("tringle is scalene")
# else:
#     print("triangle is isosceless")


# ---------> question 11 Q5<-----------

# a=int(input("enter the your persentage""\n"))
# if(a<40):
#     print("you are failed")
# elif(a>=40 and a<55):
#     print("your score is fair")
# elif(a>=55 and a<65):
#     print("your score is good")
# elif(a>=65 and a<=100):
#     print("your score is Excellent")
# else:
#     print("persentage is not correct")


# ---------> question 12 Q7<-----------

# a=int(input("enter first number" "\n"))
# b=int(input("enter second number""\n"))
# c=int(input("choose operator""\n""1=+(sum)""\n""2=-(substraction)""\n""3=*(multiplication)""\n""4=/(divison)""\n""5=%(Modulas)" "\n"))
# if(c==1):
#     d=a+b
#     print("answer is ",d)
# elif(c==2):
#     d=a-b
#     print("answer is ",d)
# elif(c==3):
#     d=a*b
#     print("answer is ",d)
# elif(c==4):
#     d=a/b
#     print("answer is ",d)
# elif(c==5):
#     d=a%b
#     print("answer is ",d)
# else:
#     print("wrong choice")